class EmployeeView:
    """Handles console inputs, menus, and formatted outputs for the Employee system."""
    def display_menu(self):
        print("\n" + "=" * 50)
        print(" EMPLOYEE MANAGEMENT SYSTEM (MVC) ")
        print("=" * 50)
        print("1. Create New Employee Record")
        print("2. View All Employee Records")
        print("3. Search Employee by ID")
        print("4. Update Employee Record")
        print("5. Delete Employee Record")
        print("6. Exit")
        print("-" * 50)
        return input("Select an option (1-6): ").strip()

    def get_employee_input(self):
        print("\n--- Enter Employee Details ---")
        emp_id = input("Employee ID: ").strip()
        name = input("Full Name: ").strip()
        designation = input("Designation: ").strip()
        department = input("Department: ").strip()
        while True:
            try:
                salary = float(input("Salary: ").strip())
                if salary >= 0:
                    break
                print("Salary cannot be negative.")
            except ValueError:
                print("Invalid input. Please enter a valid decimal number for salary.")
        return emp_id, name, designation, department, salary

    def get_emp_id(self, action_type="Search"):
        return input(f"\nEnter Employee ID to {action_type}: ").strip()

    def get_update_input(self, emp):
        print(f"\nCurrent Record -> Name: {emp[1]}, Designation: {emp[2]}, Dept: {emp[3]}, Salary: {emp[4]}")
        print("Enter new details (leave blank to keep current value):")
        name = input(f"New Name [{emp[1]}]: ").strip() or emp[1]
        designation = input(f"New Designation [{emp[2]}]: ").strip() or emp[2]
        department = input(f"New Department [{emp[3]}]: ").strip() or emp[3]
        
        sal_input = input(f"New Salary [{emp[4]}]: ").strip()
        try:
            salary = float(sal_input) if sal_input else emp[4]
            return name, designation, department, salary
        except ValueError:
            print("Invalid salary format. Keeping previous salary value.")
            return name, designation, department, emp[4]

    def confirm_deletion(self, emp_id):
        return input(f"Are you sure you want to delete employee '{emp_id}'? (y/n): ").strip().lower() == 'y'

    def display_message(self, message):
        print(f"\n{message}")

    def display_employee_table(self, employees):
        print("\n" + "=" * 90)
        print(f"{'Emp ID':<12} {'Name':<20} {'Designation':<20} {'Department':<18} {'Salary ($)':<10}")
        print("-" * 90)
        if not employees:
            print("No employee records found in the database.")
        else:
            for e in employees:
                print(f"{e[0]:<12} {e[1]:<20} {e[2]:<20} {e[3]:<18} {e[4]:<10.2f}")
        print("=" * 90)

    def display_employee_details(self, emp):
        if emp:
            print("\n" + "=" * 50)
            print(" EMPLOYEE RECORD FOUND ")
            print("=" * 50)
            print(f"Employee ID : {emp[0]}")
            print(f"Name        : {emp[1]}")
            print(f"Designation : {emp[2]}")
            print(f"Department  : {emp[3]}")
            print(f"Salary      : ${emp[4]:.2f}")
            print("=" * 50)
        else:
            print("\nEmployee record not found.")