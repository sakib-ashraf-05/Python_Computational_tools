def add_student(students):
    student_id = input("Enter Student ID: ").strip()
    if any(s['id'] == student_id for s in students):
        print("Error: Student ID already exists.")
        return
    name = input("Enter Student Name: ").strip()
    age = input("Enter Student Age: ").strip()
    grade = input("Enter Student Grade: ").strip()
    
    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "grade": grade
    }
    students.append(student)
    print("Student record added successfully.")

def delete_student(students):
    student_id = input("Enter Student ID to delete: ").strip()
    for i, student in enumerate(students):
        if student['id'] == student_id:
            del students[i]
            print("Student record deleted successfully.")
            return
    print("Error: Student ID not found.")

def search_student(students):
    query = input("Enter Student ID or Name to search: ").strip().lower()
    found = [s for s in students if query in s['id'].lower() or query in s['name'].lower()]
    
    if found:
        print("\n--- Search Results ---")
        for s in found:
            print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Grade: {s['grade']}")
    else:
        print("No matching student records found.")

def display_students(students):
    if not students:
        print("No student records available.")
        return
    print("\n--- Student Records ---")
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Grade: {s['grade']}")

def main():
    students = []
    while True:
        print("\n=== Student Record Manager ===")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Search Student")
        print("4. Display All Students")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            delete_student(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            display_students(students)
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()