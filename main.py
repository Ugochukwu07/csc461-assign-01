# Import necessary classes from the students package
from students.main import Student
from students.EnglishStudent import EnglishStudent
from students.HistoryStudent import HistoryStudent
from students.MathStudent import MathStudent

# Ask the user for input and output file names
input_file = input("Enter the input file name: ")
output_file = input("Enter the output file name: ")

# Read the student data from the input file and create student objects
students = []
with open(input_file, 'r') as file:
    num_students = int(file.readline().strip())

    # Process each student entry from the input file
    for _ in range(num_students):
        name = file.readline().strip()
        subject = file.readline().strip().split()

        last_name, first_name = name.split(', ')
        category = subject[0]
        grades = list(map(int, subject[1:]))

        # Based on the course category, create the appropriate student object
        if category == "English":
            student = EnglishStudent(first_name, last_name)
            student.set_term_paper_grade(grades[0])
            student.set_midterm_grade(grades[1])
            student.set_final_exam_grade(grades[2])
        elif category == "History":
            student = HistoryStudent(first_name, last_name)
            student.set_attendance_grade(grades[0])
            student.set_project_grade(grades[1])
            student.set_midterm_grade(grades[2])
            student.set_final_exam_grade(grades[3])
        elif category == "Math":
            student = MathStudent(first_name, last_name)
            for i in range(5):
                student.add_quiz_grade(grades[i])
            student.set_test1_grade(grades[5])
            student.set_test2_grade(grades[6])
            student.set_final_exam_grade(grades[7])

        # Add the student object to the list of students
        students.append(student)

# Compute the final averages for each student
for student in students:
    student_average = student.compute_final_average()
    student.set_final_average(student_average)

# Sort the students list based on the final averages in descending order
students.sort(key=lambda x: x.get_final_average(), reverse=True)

# Group students by course in a dictionary
students_by_course = {}
for student in students:
    course = student.get_course()
    if course not in students_by_course:
        students_by_course[course] = []
    students_by_course[course].append(student)

# Print the summary report to the output file grouped by course
# ... (Previous code remains the same)

# Print the summary report to the output file grouped by course
with open(output_file, 'w') as file:
    file.writelines("Student Grade Summary\n")
    file.writelines("---------------------\n\n")

    for course, students_list in students_by_course.items():
        file.write(f"{course} CLASS\n")
        file.write(f"{'Student': <40}{'Final Exam': <10}{'Final Avg': <10}{'Letter Grade':}\n")
        file.write(f"{'Name': <40}{'Grade': <10}{'Grade': <10}{'':}\n")
        file.write(f"{'-' * 61}\n")

        for student in students_list:
            file.write(f"{student.get_first_name()} {student.get_last_name(): <34}")
            file.write(f"{student.get_final_exam_grade(): <10}")
            file.write(f"{student.get_final_average():.2f}{'': <10}")
            file.write(f"{student.get_letter_grade()}\n")

        file.write("\n")

    # Calculate grade distribution
    grades = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'F': 0
    }
    for student in students:
        letter_grade = student.get_letter_grade()
        grades[letter_grade] += 1

    # Write grade distribution to the output file
    file.write("OVERALL GRADE DISTRIBUTION\n")
    for grade, count in grades.items():
        file.write(f"{grade}: {count}\n")
