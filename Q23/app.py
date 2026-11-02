import os
import xml.etree.ElementTree as ET

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(BASE_DIR, "students.xml")
UPDATED_FILE = os.path.join(BASE_DIR, "students_updated.xml")
REPORT_FILE = os.path.join(BASE_DIR, "department_report.xml")

def load_xml(path):
    """Parse an XML file and return its tree."""
    return ET.parse(path)


def save_xml(tree, path):
    """Save a tree to disk with indentation."""
    ET.indent(tree, space="    ")
    tree.write(path, encoding="UTF-8", xml_declaration=True)
    print(f"Saved -> {path}")


# ---------- Read ----------
def find_student(root, student_id):
    return root.find(f"./student[@id='{student_id}']")


def display_students(root, title="Students"):
    print(f"\n{title}")
    print("-" * 78)
    print(f"{'ID':<6}{'Name':<18}{'Dept':<7}{'Year':<6}{'CGPA':<7}Email")
    print("-" * 78)
    for s in root.findall("student"):
        print(f"{s.get('id'):<6}{s.findtext('name'):<18}{s.findtext('department'):<7}"
              f"{s.findtext('year'):<6}{s.findtext('cgpa'):<7}{s.findtext('email')}")


def search_by_name(root, keyword):
    return [s for s in root.findall("student")
            if keyword.lower() in s.findtext("name").lower()]


def filter_by_department(root, dept):
    return [s for s in root.findall("student")
            if s.findtext("department").upper() == dept.upper()]


# ---------- Create ----------
def add_student(root, student_id, name, department, year, email, cgpa):
    if find_student(root, student_id) is not None:
        print(f"Student {student_id} already exists - not added.")
        return None
    student = ET.SubElement(root, "student", id=str(student_id))
    for tag, value in [("name", name), ("department", department),
                       ("year", year), ("email", email), ("cgpa", cgpa)]:
        ET.SubElement(student, tag).text = str(value)
    print(f"Added student {student_id} ({name})")
    return student


# ---------- Update ----------
def update_student(root, student_id, **fields):
    student = find_student(root, student_id)
    if student is None:
        print(f"Student {student_id} not found.")
        return False
    for tag, value in fields.items():
        element = student.find(tag)
        if element is None:
            element = ET.SubElement(student, tag)  # add the field if missing
        element.text = str(value)
    print(f"Updated student {student_id}: {fields}")
    return True


# ---------- Delete ----------
def delete_student(root, student_id):
    student = find_student(root, student_id)
    if student is None:
        print(f"Student {student_id} not found.")
        return False
    root.remove(student)
    print(f"Deleted student {student_id}")
    return True


# ---------- Generate a new XML document ----------
def generate_department_report(root):
    """Build a brand-new XML document grouping students by department."""
    report = ET.Element("department_report")
    departments = sorted({s.findtext("department") for s in root.findall("student")})

    for dept in departments:
        members = filter_by_department(root, dept)
        cgpas = [float(s.findtext("cgpa")) for s in members]
        dept_el = ET.SubElement(report, "department", name=dept,
                                count=str(len(members)),
                                average_cgpa=f"{sum(cgpas) / len(cgpas):.2f}")
        for s in sorted(members, key=lambda x: float(x.findtext("cgpa")), reverse=True):
            ET.SubElement(dept_el, "student", id=s.get("id"),
                          name=s.findtext("name"), cgpa=s.findtext("cgpa"))
    return ET.ElementTree(report)

MENU = """
===== Student XML Manager =====
1. Display all students
2. Search by name
3. Filter by department
4. Add student
5. Update student
6. Delete student
7. Generate department report
8. Save changes
0. Exit
"""


def print_list(students, title):
    if not students:
        print("No matching students.")
        return
    wrapper = ET.Element("students")
    wrapper.extend(students)
    display_students(wrapper, title)


def main():
    tree = load_xml(INPUT_FILE)
    root = tree.getroot()
    changed = False

    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            display_students(root, "All students")
        elif choice == "2":
            print_list(search_by_name(root, input("Name contains: ")), "Search results")
        elif choice == "3":
            print_list(filter_by_department(root, input("Department: ")), "Department students")
        elif choice == "4":
            sid = input("ID: ").strip()
            changed |= add_student(root, sid, input("Name: "), input("Department: "),
                                   input("Year: "), input("Email: "), input("CGPA: ")) is not None
        elif choice == "5":
            sid = input("ID: ").strip()
            field = input("Field (name/department/year/email/cgpa): ").strip().lower()
            changed |= update_student(root, sid, **{field: input("New value: ")})
        elif choice == "6":
            changed |= delete_student(root, input("ID: ").strip())
        elif choice == "7":
            save_xml(generate_department_report(root), REPORT_FILE)
        elif choice == "8":
            save_xml(tree, UPDATED_FILE)
            changed = False
        elif choice == "0":
            if changed and input("Save unsaved changes? (y/n): ").lower() == "y":
                save_xml(tree, UPDATED_FILE)
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()