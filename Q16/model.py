import sqlite3

class StudentModel:
    """Handles SQLite database connection, table creation, and CRUD operations."""
    def __init__(self, db_name="students.db"):
        self.db_name = db_name
        self.create_table()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                roll_number TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                department TEXT NOT NULL,
                cgpa REAL NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def add_student(self, roll_number, name, department, cgpa):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO students (roll_number, name, department, cgpa)
                VALUES (?, ?, ?, ?)
            ''', (roll_number, name, department, cgpa))
            conn.commit()
            conn.close()
            return True, "Student added successfully."
        except sqlite3.IntegrityError:
            return False, "Error: Roll number already exists."
        except Exception as e:
            return False, f"An error occurred: {e}"

    def get_all_students(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT roll_number, name, department, cgpa FROM students')
        students = cursor.fetchall()
        conn.close()
        return students

    def get_student_by_roll(self, roll_number):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT roll_number, name, department, cgpa FROM students WHERE roll_number = ?', (roll_number,))
        student = cursor.fetchone()
        conn.close()
        return student