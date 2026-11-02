class SalaryReportView:
    """Handles console inputs, menus, and formatted tabular outputs for salary reports."""
    def display_menu(self):
        print("\n" + "=" * 55)
        print(" EMPLOYEE SALARY REPORT SYSTEM (MVC) ")
        print("=" * 55)
        print("1. View Department-Wise Salary Summary Report")
        print("2. View Detailed Employee Report by Specific Department (Parameterized)")
        print("3. Exit")
        print("-" * 55)
        return input("Select an option (1-3): ").strip()

    def get_department_choice(self, departments):
        print("\nAvailable Departments:")
        for idx, dept in enumerate(departments, 1):
            print(f"  {idx}. {dept}")
        
        dept_input = input("Enter department name or number: ").strip()
        
        # Resolve number selection to department name if applicable
        if dept_input.isdigit():
            idx = int(dept_input) - 1
            if 0 <= idx < len(departments):
                return departments[idx]
        return dept_input

    def display_summary_report(self, summary_data):
        print("\n" + "=" * 100)
        print(" DEPARTMENT-WISE SALARY SUMMARY REPORT ")
        print("=" * 100)
        print(f"{'Department':<18} {'Emp Count':<12} {'Total Salary ($)':<18} {'Avg Salary ($)':<18} {'Max ($)':<12} {'Min ($)':<12}")
        print("-" * 100)
        if not summary_data:
            print("No department records found.")
        else:
            for row in summary_data:
                dept, count, total, avg, mx, mn = row
                print(f"{dept:<18} {count:<12} {total:<18.2f} {avg:<18.2f} {mx:<12.2f} {mn:<12.2f}")
        print("=" * 100)

    def display_detail_report(self, department_name, employees):
        print("\n" + "=" * 80)
        print(f" DETAILED SALARY REPORT FOR DEPARTMENT: {department_name.upper()} ")
        print("=" * 80)
        print(f"{'Emp ID':<12} {'Name':<22} {'Designation':<25} {'Salary ($)':<15}")
        print("-" * 80)
        if not employees:
            print(f"No employee records found for department '{department_name}'.")
        else:
            total_dept_salary = 0
            for emp in employees:
                emp_id, name, desig, salary = emp
                total_dept_salary += salary
                print(f"{emp_id:<12} {name:<22} {desig:<25} ${salary:<14.2f}")
            print("-" * 80)
            print(f"Total Department Expenditure: ${total_dept_salary:,.2f}")
        print("=" * 80)

    def display_message(self, message):
        print(f"\n{message}")