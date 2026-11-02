import tkinter as tk
from tkinter import ttk

class LibraryView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Library Management System - MVC")
        self.geometry("850x550")
        self.config(bg="#f4f6f9")
        
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title_lbl = tk.Label(self, text="Library Management System", font=("Arial", 18, "bold"), bg="#f4f6f9", fg="#333")
        title_lbl.pack(pady=10)

        # Main Frame Split Layout
        main_frame = tk.Frame(self, bg="#f4f6f9")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

        # Left Panel: Form Inputs & Actions
        left_frame = tk.LabelFrame(main_frame, text=" Book Operations ", font=("Arial", 11, "bold"), bg="#f4f6f9", padx=10, pady=10)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        tk.Label(left_frame, text="Book Title:", bg="#f4f6f9").pack(anchor="w", pady=(5, 0))
        self.title_entry = tk.Entry(left_frame, width=25, font=("Arial", 11))
        self.title_entry.pack(pady=2)

        tk.Label(left_frame, text="Author:", bg="#f4f6f9").pack(anchor="w", pady=(5, 0))
        self.author_entry = tk.Entry(left_frame, width=25, font=("Arial", 11))
        self.author_entry.pack(pady=2)

        tk.Label(left_frame, text="ISBN:", bg="#f4f6f9").pack(anchor="w", pady=(5, 0))
        self.isbn_entry = tk.Entry(left_frame, width=25, font=("Arial", 11))
        self.isbn_entry.pack(pady=2)

        tk.Label(left_frame, text="Borrower Name (for Issue):", bg="#f4f6f9").pack(anchor="w", pady=(10, 0))
        self.borrower_entry = tk.Entry(left_frame, width=25, font=("Arial", 11))
        self.borrower_entry.pack(pady=2)

        # Action Buttons
        self.add_btn = tk.Button(left_frame, text="Add Book", bg="#28a745", fg="white", font=("Arial", 10, "bold"), width=22)
        self.add_btn.pack(pady=(15, 5))

        self.issue_btn = tk.Button(left_frame, text="Issue Selected Book", bg="#ffc107", fg="black", font=("Arial", 10, "bold"), width=22)
        self.issue_btn.pack(pady=5)

        self.return_btn = tk.Button(left_frame, text="Return Selected Book", bg="#17a2b8", fg="white", font=("Arial", 10, "bold"), width=22)
        self.return_btn.pack(pady=5)

        # Right Panel: Search and Record Table Display
        right_frame = tk.Frame(main_frame, bg="#f4f6f9")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Search Sub-frame
        search_frame = tk.Frame(right_frame, bg="#f4f6f9")
        search_frame.pack(fill=tk.X, pady=5)

        tk.Label(search_frame, text="Search:", bg="#f4f6f9", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=2)
        self.search_entry = tk.Entry(search_frame, width=25, font=("Arial", 11))
        self.search_entry.pack(side=tk.LEFT, padx=5)

        self.search_btn = tk.Button(search_frame, text="Search", bg="#007bff", fg="white", font=("Arial", 9, "bold"))
        self.search_btn.pack(side=tk.LEFT, padx=5)

        self.refresh_btn = tk.Button(search_frame, text="Refresh List", bg="#6c757d", fg="white", font=("Arial", 9, "bold"))
        self.refresh_btn.pack(side=tk.LEFT, padx=5)

        # Treeview Table for Records
        columns = ("ID", "Title", "Author", "ISBN", "Status", "Borrower")
        self.tree = ttk.Treeview(right_frame, columns=columns, show="headings", height=15)
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=90, anchor=tk.CENTER)
        self.tree.column("Title", width=140)
        self.tree.column("Author", width=120)

        scrollbar = ttk.Scrollbar(right_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, pady=5)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=5)

    def clear_inputs(self):
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.isbn_entry.delete(0, tk.END)
        self.borrower_entry.delete(0, tk.END)

    def get_selected_book_id(self):
        selected_item = self.tree.selection()
        if not selected_item:
            return None
        item_values = self.tree.item(selected_item[0], "values")
        return int(item_values[0])