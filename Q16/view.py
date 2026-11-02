class StudentView:
    """Handles console inputs, menus, and formatted outputs for the user."""
    def display_menu(self):
        print("\n" + "=" * 45)
        print(" STUDENT INFORMATION MANAGEMENT SYSTEM (MVC) ")
        print("=" * 45)
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search Student by Roll Number")
        print("4. Exit")
        print("-" * 45)
        return input("Select an option (1-4): ").strip()

    def get_student_input(self):
        print("\n--- Enter Student Details ---")
        roll = input("Roll Number: ").strip()
        name = input("Full Name: ").strip()
        dept = input("Department: ").strip()
        while True:
            try:
                cgpa = float(input("CGPA (0.0 - 10.0): ").strip())
                if 0.0 <= cgpa <= 10.0:
                    break
                print("CGPA must be between 0.0 and 10.0.")
            except ValueError:
                print("Invalid input. Please enter a valid decimal number for CGPA.")
        return roll, name, dept, cgpa

    def get_roll_number(self):
        return input("\nEnter Roll Number to Search: ").strip()

    def display_message(self, message):
        print(f"\n{message}")

    def display_student_list(self, students):
        print("\n" + "=" * 70)
        print(f"{'Roll Number':<15} {'Name':<20} {'Department':<18} {'CGPA':<6}")
        print("-" * 70)
        if not students:
            print("No student records found.")
        else:
            for s in students:
                print(f"{s[0]:<15} {s[1]:<20} {s[2]:<18} {s[3]:<6.2f}")
        print("=" * 70)

    def display_student_details(self, student):
        if student:
            print("\n" + "=" * 50)
            print(" STUDENT RECORD FOUND ")
            print("=" * 50)
            print(f"Roll Number : {student[0]}")
            print(f"Name        : {student[1]}")
            print(f"Department  : {student[2]}")
            print(f"CGPA        : {student[3]:.2f}")
            print("=" * 50)
        else:
            print("\nStudent record not found.")