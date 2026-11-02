import sqlite3

class LibraryModel:
    def __init__(self, db_name="library.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    isbn TEXT UNIQUE NOT NULL,
                    status TEXT DEFAULT 'Available',
                    borrower TEXT
                )
            ''')

    def add_book(self, title, author, isbn):
        if not title or not author or not isbn:
            return False, "All fields are required."
        try:
            with self.conn:
                self.conn.execute(
                    "INSERT INTO books (title, author, isbn, status) VALUES (?, ?, ?, 'Available')",
                    (title, author, isbn)
                )
            return True, "Book added successfully."
        except sqlite3.IntegrityError:
            return False, "A book with this ISBN already exists."

    def search_books(self, query=""):
        cursor = self.conn.cursor()
        search_term = f"%{query}%"
        cursor.execute(
            "SELECT id, title, author, isbn, status, COALESCE(borrower, '') FROM books WHERE title LIKE ? OR author LIKE ? OR isbn LIKE ?",
            (search_term, search_term, search_term)
        )
        return cursor.fetchall()

    def issue_book(self, book_id, borrower):
        if not borrower:
            return False, "Borrower name is required to issue a book."
        cursor = self.conn.cursor()
        cursor.execute("SELECT status FROM books WHERE id = ?", (book_id,))
        row = cursor.fetchone()
        
        if not row:
            return False, "Selected book not found."
        if row[0] == 'Issued':
            return False, "Book is already issued."

        with self.conn:
            self.conn.execute(
                "UPDATE books SET status = 'Issued', borrower = ? WHERE id = ?",
                (borrower, book_id)
            )
        return True, "Book issued successfully."

    def return_book(self, book_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT status FROM books WHERE id = ?", (book_id,))
        row = cursor.fetchone()
        
        if not row:
            return False, "Selected book not found."
        if row[0] == 'Available':
            return False, "Book is already available in the library."

        with self.conn:
            self.conn.execute(
                "UPDATE books SET status = 'Available', borrower = NULL WHERE id = ?",
                (book_id,)
            )
        return True, "Book returned successfully."

    def __del__(self):
        if hasattr(self, 'conn'):
            self.conn.close()