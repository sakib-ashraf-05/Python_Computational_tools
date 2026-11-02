import tkinter as tk
from tkinter import messagebox

class LibraryController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Bind View events to Controller methods
        self.view.add_btn.config(command=self.add_book)
        self.view.search_btn.config(command=self.search_books)
        self.view.refresh_btn.config(command=self.load_books)
        self.view.issue_btn.config(command=self.issue_book)
        self.view.return_btn.config(command=self.return_book)

        # Initial load of data into the table
        self.load_books()

    def load_books(self):
        self.update_table(self.model.search_books(""))

    def update_table(self, records):
        for row in self.view.tree.get_children():
            self.view.tree.delete(row)
        for record in records:
            self.view.tree.insert("", tk.END, values=record)

    def add_book(self):
        title = self.view.title_entry.get().strip()
        author = self.view.author_entry.get().strip()
        isbn = self.view.isbn_entry.get().strip()

        success, message = self.model.add_book(title, author, isbn)
        if success:
            messagebox.showinfo("Success", message)
            self.view.clear_inputs()
            self.load_books()
        else:
            messagebox.showerror("Error", message)

    def search_books(self):
        query = self.view.search_entry.get().strip()
        records = self.model.search_books(query)
        self.update_table(records)

    def issue_book(self):
        book_id = self.view.get_selected_book_id()
        if not book_id:
            messagebox.showwarning("Selection Warning", "Please select a book from the table to issue.")
            return

        borrower = self.view.borrower_entry.get().strip()
        success, message = self.model.issue_book(book_id, borrower)
        if success:
            messagebox.showinfo("Success", message)
            self.view.borrower_entry.delete(0, tk.END)
            self.load_books()
        else:
            messagebox.showerror("Error", message)

    def return_book(self):
        book_id = self.view.get_selected_book_id()
        if not book_id:
            messagebox.showwarning("Selection Warning", "Please select a book from the table to return.")
            return

        success, message = self.model.return_book(book_id)
        if success:
            messagebox.showinfo("Success", message)
            self.load_books()
        else:
            messagebox.showerror("Error", message)