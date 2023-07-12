# Import the required classes and functions
from student import EnglishStudent, HistoryStudent, MathStudent
from grade_functions import write_student_info, write_grade_distribution

# Ask the user for input and output file names
input_file = input("Enter the input file name: ")
output_file = input("Enter the output file name: ")

# Read the student data from the input file
students = []
with open(input_file, 'r') as file:
    num_students = int(file.readline().strip())

    for _ in range(num_students):
        name = file.readline().strip()
        subject = file.readline().strip().split()

        last_name, first_name = name.split(', ')
        category = subject[0]
        grades = list(map(int, subject[1:]))

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

        students.append(student)

# Compute the final averages for each student
for student in students:
    student_average = student.compute_final_average()
    student.set_final_average(student_average)

# Sort the students list based on the final averages
students.sort(key=lambda x: x.get_final_average(), reverse=True)

# Grade distribution
grades = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'F': 0
}

# Print the summary report to the output file
with open(output_file, 'w') as file:
    for student in students:
        write_student_info(file, student)
        letter_grade = student.get_letter_grade()
        grades[letter_grade] += 1

    write_grade_distribution(file, grades)
