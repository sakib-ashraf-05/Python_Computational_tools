class EmployeeController:
    """Coordinates interactions between the Employee Model and View."""
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        while True:
            choice = self.view.display_menu()
            if choice == '1':
                emp_id, name, desig, dept, salary = self.view.get_employee_input()
                success, msg = self.model.create_employee(emp_id, name, desig, dept, salary)
                self.view.display_message(msg)
            elif choice == '2':
                employees = self.model.read_all_employees()
                self.view.display_employee_table(employees)
            elif choice == '3':
                emp_id = self.view.get_emp_id("Search")
                emp = self.model.read_employee_by_id(emp_id)
                self.view.display_employee_details(emp)
            elif choice == '4':
                emp_id = self.view.get_emp_id("Update")
                emp = self.model.read_employee_by_id(emp_id)
                if not emp:
                    self.view.display_message(f"Error: Employee ID '{emp_id}' does not exist.")
                else:
                    name, desig, dept, salary = self.view.get_update_input(emp)
                    success, msg = self.model.update_employee(emp_id, name, desig, dept, salary)
                    self.view.display_message(msg)
            elif choice == '5':
                emp_id = self.view.get_emp_id("Delete")
                if self.view.confirm_deletion(emp_id):
                    success, msg = self.model.delete_employee(emp_id)
                    self.view.display_message(msg)
                else:
                    self.view.display_message("Deletion cancelled.")
            elif choice == '6':
                self.view.display_message("Exiting system. Goodbye!")
                break
            else:
                self.view.display_message("Invalid option. Please choose a number between 1 and 6.")