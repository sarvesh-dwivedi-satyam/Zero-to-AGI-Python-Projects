def manage_student_records():
    student_db = {}
    student_name = input("Enter Student Name: ").strip().title()
    initial_marks = float(input("Enter Initial Marks: "))
    student_db[student_name] = initial_marks
    print(f"Record Created: {student_db}")
    updated_marks = float(input(f"Enter Updated Marks for {student_name}: "))
    student_db[student_name] = updated_marks
    print(f"Final Updated Database Matrix: {student_db}")
if __name__ == '__main__':
    manage_student_records ()