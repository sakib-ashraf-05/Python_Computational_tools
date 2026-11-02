import xml.etree.ElementTree as ET


def parse_university_xml(file_path):
  print(f"========================================================")
  print(f" PARSING XML DOCUMENT: {file_path}")
  print(f"========================================================\n")

  try:
    tree = ET.parse(file_path)
    root = tree.getroot()

    # University Overview
    uni_name = root.get("name", "N/A")
    campus = root.find("campus")
    location = (
        campus.find("location").text
        if campus is not None and campus.find("location") is not None
        else "N/A"
    )
    established = (
        campus.find("established").text
        if campus is not None and campus.find("established") is not None
        else "N/A"
    )
    website = (
        campus.find("website").text
        if campus is not None and campus.find("website") is not None
        else "N/A"
    )

    print(f"University: {uni_name}")
    print(
        f"Location:   {location}\nEstablished: {established}\nWebsite:    "
        f" {website}\n"
    )

    departments = root.find("departments")
    if departments is not None:
      for dept in departments.findall("department"):
        dept_id = dept.get("id", "N/A")
        dept_name = (
            dept.find("name").text
            if dept.find("name") is not None
            else "Unnamed Department"
        )
        hod = dept.find("hod").text if dept.find("hod") is not None else "N/A"
        building = (
            dept.find("building").text
            if dept.find("building") is not None
            else "N/A"
        )

        print(f"--------------------------------------------------------")
        print(f"DEPARTMENT: [{dept_id}] {dept_name}")
        print(f"HOD: {hod}  |  Building: {building}")
        print(f"--------------------------------------------------------")

        students = dept.find("students")
        if students is not None:
          for student in students.findall("student"):
            stud_id = student.get("id", "N/A")
            p_details = student.find("personal_details")
            a_details = student.find("academic_details")

            # Extract student name safely
            name_elem = p_details.find("name") if p_details is not None else None
            f_name = (
                name_elem.find("first_name").text
                if name_elem is not None
                and name_elem.find("first_name") is not None
                else ""
            )
            l_name = (
                name_elem.find("last_name").text
                if name_elem is not None
                and name_elem.find("last_name") is not None
                else ""
            )
            full_name = f"{f_name} {l_name}".strip()

            gender = (
                p_details.find("gender").text
                if p_details is not None and p_details.find("gender") is not None
                else "N/A"
            )
            email = (
                p_details.find("email").text
                if p_details is not None and p_details.find("email") is not None
                else "N/A"
            )

            year = (
                a_details.find("year").text
                if a_details is not None and a_details.find("year") is not None
                else "N/A"
            )
            semester = (
                a_details.find("semester").text
                if a_details is not None
                and a_details.find("semester") is not None
                else "N/A"
            )
            cgpa = (
                a_details.find("cgpa").text
                if a_details is not None and a_details.find("cgpa") is not None
                else "N/A"
            )
            advisor = (
                a_details.find("advisor").text
                if a_details is not None
                and a_details.find("advisor") is not None
                else "N/A"
            )

            print(f"  • Student ID: {stud_id} | Name: {full_name}")
            print(
                f"    Gender: {gender} | Email: {email} | Year/Sem: Year"
                f" {year}, Sem {semester} | CGPA: {cgpa} | Advisor: {advisor}"
            )

            # Courses Table
            courses = a_details.find("courses") if a_details is not None else None
            if courses is not None:
              print(f"    Enrolled Courses:")
              print(
                  f"      {'Code':<8} | {'Course Name':<32} | {'Credits':<7}"
                  f" | {'Marks':<5} | {'Grade':<5}"
              )
              print(f"      " + "-" * 67)
              for course in courses.findall("course"):
                code = course.get("code", "N/A")
                c_name = (
                    course.find("name").text
                    if course.find("name") is not None
                    else "N/A"
                )
                credits = (
                    course.find("credits").text
                    if course.find("credits") is not None
                    else "N/A"
                )
                marks = (
                    course.find("marks").text
                    if course.find("marks") is not None
                    else "N/A"
                )
                grade = (
                    course.find("grade").text
                    if course.find("grade") is not None
                    else "N/A"
                )
                print(
                    f"      {code:<8} | {c_name:<32} | {credits:<7} |"
                    f" {marks:<5} | {grade:<5}"
                )
            print()

  except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
  except ET.ParseError:
    print(f"Error: Failed to parse XML structure from '{file_path}'.")


if __name__ == "__main__":
    xml_filename = "university_records.xml"
    parse_university_xml(xml_filename)