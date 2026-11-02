class SalaryReportController:
    """Coordinates interactions between the Salary Report Model and View."""
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        while True:
            choice = self.view.display_menu()
            
            if choice == '1':
                summary = self.model.get_department_summary_report()
                self.view.display_summary_report(summary)
                
            elif choice == '2':
                departments = self.model.get_all_departments()
                if not departments:
                    self.view.display_message("No departments available in the database.")
                    continue
                
                target_dept = self.view.get_department_choice(departments)
                employees = self.model.get_department_detail_report(target_dept)
                self.view.display_detail_report(target_dept, employees)
                
            elif choice == '3':
                self.view.display_message("Exiting salary reporting system. Goodbye!")
                break
            else:
                self.view.display_message("Invalid option. Please choose a number between 1 and 3.")