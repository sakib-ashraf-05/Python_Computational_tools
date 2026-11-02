import sqlite3

class EmployeeModel:
    """Handles SQLite database connection, table creation, and CRUD operations for employees."""
    def __init__(self, db_name="employees.db"):
        self.db_name = db_name
        self.create_table()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                emp_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                designation TEXT NOT NULL,
                department TEXT NOT NULL,
                salary REAL NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def create_employee(self, emp_id, name, designation, department, salary):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO employees (emp_id, name, designation, department, salary)
                VALUES (?, ?, ?, ?, ?)
            ''', (emp_id, name, designation, department, salary))
            conn.commit()
            conn.close()
            return True, "Employee added successfully."
        except sqlite3.IntegrityError:
            return False, f"Error: Employee ID '{emp_id}' already exists."
        except Exception as e:
            return False, f"An error occurred: {e}"

    def read_all_employees(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT emp_id, name, designation, department, salary FROM employees')
        employees = cursor.fetchall()
        conn.close()
        return employees

    def read_employee_by_id(self, emp_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT emp_id, name, designation, department, salary FROM employees WHERE emp_id = ?', (emp_id,))
        employee = cursor.fetchone()
        conn.close()
        return employee

    def update_employee(self, emp_id, name, designation, department, salary):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE employees
            SET name = ?, designation = ?, department = ?, salary = ?
            WHERE emp_id = ?
        ''', (name, designation, department, salary, emp_id))
        conn.commit()
        rows_affected = cursor.rowcount
        conn.close()
        if rows_affected > 0:
            return True, "Employee record updated successfully."
        else:
            return False, "Error: Employee ID not found."

    def delete_employee(self, emp_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM employees WHERE emp_id = ?', (emp_id,))
        conn.commit()
        rows_affected = cursor.rowcount
        conn.close()
        if rows_affected > 0:
            return True, "Employee record deleted successfully."
        else:
            return False, "Error: Employee ID not found."