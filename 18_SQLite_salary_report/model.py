import sqlite3

class SalaryReportModel:
    """Handles SQLite database setup, sample data seeding, and parameterized queries for salary reports."""
    def __init__(self, db_name="employees.db"):
        self.db_name = db_name
        self.setup_database()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def setup_database(self):
        """Creates the employee table and seeds sample data if the table is empty."""
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
        
        # Check if table is empty to seed sample records
        cursor.execute('SELECT COUNT(*) FROM employees')
        if cursor.fetchone()[0] == 0:
            sample_data = [
                ('E001', 'Alice Smith', 'Software Engineer', 'Engineering', 85000.0),
                ('E002', 'Bob Jones', 'Senior Developer', 'Engineering', 115000.0),
                ('E003', 'Charlie Brown', 'HR Manager', 'Human Resources', 75000.0),
                ('E004', 'Diana Prince', 'Recruiter', 'Human Resources', 60000.0),
                ('E005', 'Evan Wright', 'Sales Executive', 'Sales', 65000.0),
                ('E006', 'Fiona Gallagher', 'Sales Manager', 'Sales', 95000.0),
                ('E007', 'George Clark', 'DevOps Engineer', 'Engineering', 90000.0),
                ('E008', 'Hannah Abbott', 'Financial Analyst', 'Finance', 80000.0)
            ]
            cursor.executemany('''
                INSERT INTO employees (emp_id, name, designation, department, salary)
                VALUES (?, ?, ?, ?, ?)
            ''', sample_data)
            conn.commit()
        conn.close()

    def get_all_departments(self):
        """Retrieves a list of distinct departments from the database."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT DISTINCT department FROM employees ORDER BY department')
        departments = [row[0] for row in cursor.fetchall()]
        conn.close()
        return departments

    def get_department_summary_report(self):
        """Executes an aggregate query to summarize employee count and salaries per department."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT department, 
                   COUNT(*) as emp_count, 
                   SUM(salary) as total_salary, 
                   AVG(salary) as avg_salary,
                   MAX(salary) as max_salary,
                   MIN(salary) as min_salary
            FROM employees 
            GROUP BY department
            ORDER BY total_salary DESC
        ''')
        report = cursor.fetchall()
        conn.close()
        return report

    def get_department_detail_report(self, department_name):
        """Executes a parameterized SQL query to fetch employees belonging to a specific department."""
        conn = self.connect()
        cursor = conn.cursor()
        # Parameterized query to safely prevent SQL injection
        cursor.execute('''
            SELECT emp_id, name, designation, salary 
            FROM employees 
            WHERE department = ? 
            ORDER BY salary DESC
        ''', (department_name,))
        employees = cursor.fetchall()
        conn.close()
        return employees