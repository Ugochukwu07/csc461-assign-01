from .main import Student

class HistoryStudent(Student):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name, "History")
        self._attendance_grade = 0
        self._project_grade = 0
        self._midterm_grade = 0
        self._final_exam_grade = 0
        self._final_average = 0

    def set_attendance_grade(self, grade):
        self._attendance_grade = grade

    def set_project_grade(self, grade):
        self._project_grade = grade

    def set_midterm_grade(self, grade):
        self._midterm_grade = grade

    def set_final_exam_grade(self, grade):
        self._final_exam_grade = grade

    
    def set_final_average(self, grade):
        self._final_average = grade

    def get_final_exam_grade(self):
        return self._final_exam_grade

    def get_final_average(self):
        return self.compute_final_average()

    def get_letter_grade(self):
        average_score = self.compute_final_average()
        if average_score >= 90:
            grade = 'A'
        elif average_score >= 80:
            grade = 'B'
        elif average_score >= 70:
            grade = 'C'
        elif average_score >= 60:
            grade = 'D'
        else:
            grade = 'F'

        return grade


    def compute_final_average(self):
        attendance_weight = 0.1
        project_weight = 0.3
        midterm_weight = 0.3
        final_exam_weight = 0.3

        final_average = (
            self._attendance_grade * attendance_weight +
            self._project_grade * project_weight +
            self._midterm_grade * midterm_weight +
            self._final_exam_grade * final_exam_weight
        )

        return final_average

