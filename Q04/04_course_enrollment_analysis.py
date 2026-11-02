def analyze_enrollments():
    # Using tuples to store student details: (student_id, name)
    alice = (101, "Alice")
    bob = (102, "Bob")
    charlie = (103, "Charlie")
    david = (104, "David")
    eva = (105, "Eva")

    # Defining course enrollments using sets containing student tuples
    python_course = {alice, bob, charlie, david}
    data_science_course = {bob, charlie, eva}
    web_dev_course = {alice, david, eva}

    print("=== Student Course Enrollment Analysis ===\n")
    
    print("Course Rosters:")
    print(f"- Python Course: {[s[1] for s in python_course]}")
    print(f"- Data Science Course: {[s[1] for s in data_science_course]}")
    print(f"- Web Development Course: {[s[1] for s in web_dev_course]}\n")
    print("-" * 50)

    # 1. Union: All unique students across all courses
    all_students = python_course.union(data_science_course, web_dev_course)
    print(f"\n1. Union (All Unique Students Across All Courses):")
    print(f"   Total Count: {len(all_students)}")
    print(f"   Students: {[(s[0], s[1]) for s in all_students]}")

    # 2. Intersection: Students enrolled in both Python and Data Science
    common_python_ds = python_course.intersection(data_science_course)
    print(f"\n2. Intersection (Students Enrolled in BOTH Python & Data Science):")
    print(f"   Students: {[(s[0], s[1]) for s in common_python_ds]}")

    # 3. Difference: Students in Python course who are NOT in Data Science
    python_not_ds = python_course.difference(data_science_course)
    print(f"\n3. Difference (Students in Python Course ONLY, excluding Data Science):")
    print(f"   Students: {[(s[0], s[1]) for s in python_not_ds]}")

    # 4. Symmetric Difference: Students enrolled in Python or Web Dev, but not both
    sym_diff = python_course.symmetric_difference(web_dev_course)
    print(f"\n4. Symmetric Difference (Students in Python OR Web Dev, but not in both):")
    print(f"   Students: {[(s[0], s[1]) for s in sym_diff]}")

if __name__ == "__main__":
    analyze_enrollments()