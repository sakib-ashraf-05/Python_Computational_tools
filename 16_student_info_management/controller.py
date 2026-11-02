class StudentController:
    """Acts as the intermediary between the Model and View."""
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        while True:
            choice = self.view.display_menu()
            if choice == '1':
                roll, name, dept, cgpa = self.view.get_student_input()
                success, msg = self.model.add_student(roll, name, dept, cgpa)
                self.view.display_message(msg)
            elif choice == '2':
                students = self.model.get_all_students()
                self.view.display_student_list(students)
            elif choice == '3':
                roll = self.view.get_roll_number()
                student = self.model.get_student_by_roll(roll)
                self.view.display_student_details(student)
            elif choice == '4':
                self.view.display_message("Exiting system. Goodbye!")
                break
            else:
                self.view.display_message("Invalid option. Please choose a number between 1 and 4.")