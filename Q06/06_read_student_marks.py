def calculate_grade(average):
    """Determines the letter grade based on the average mark."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def process_student_marks(input_filename, output_filename):
    """Reads student marks from an input file, computes totals, averages, and grades,
    and writes a cleanly formatted report to an output file.
    """
    try:
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()
            
        if not lines:
            print(f"The input file '{input_filename}' is empty.")
            return

        output_lines = []
        
        # Format headers for the output file
        title = f"STUDENT PERFORMANCE REPORT\nSource File: {input_filename}\n"
        separator = "=" * 50 + "\n"
        header_str = f"{'Name':<15} {'Total':<10} {'Average':<10} {'Grade':<6}\n"
        
        output_lines.append(title)
        output_lines.append(separator)
        output_lines.append(header_str)
        output_lines.append("-" * 50 + "\n")
        
        # Skip the header row and process each student record
        for line in lines[1:]:
            if not line.strip():
                continue
            
            parts = [p.strip() for p in line.split(',')]
            name = parts[0]
            
            try:
                marks = [float(m) for m in parts[1:]]
            except ValueError:
                print(f"Warning: Skipping line due to invalid mark format: {line.strip()}")
                continue
                
            total = sum(marks)
            average = total / len(marks) if marks else 0
            grade = calculate_grade(average)
            
            row_str = f"{name:<15} {total:<10.2f} {average:<10.2f} {grade:<6}\n"
            output_lines.append(row_str)
            
        output_lines.append(separator)
        
        with open(output_filename, 'w') as outfile:
            outfile.writelines(output_lines)
            
        print(f"Processing complete. Results successfully written to '{output_filename}'.")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = "students.txt"
    output_file = "student_results.txt"
    
    # Creating a sample input file for demonstration purposes
    sample_data = (
        "Name,Math,Science,English\n"
        "Alice Smith,85,92,78\n"
        "Bob Jones,72,65,70\n"
        "Charlie Brown,95,88,92\n"
        "Diana Prince,60,55,58\n"
    )
    
    with open(input_file, 'w') as f:
        f.write(sample_data)
        
    # Execute the processing function
    process_student_marks(input_file, output_file)