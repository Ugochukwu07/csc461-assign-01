from .main import Student

class MathStudent(Student):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name, "Math")
        self._quiz_grades = []
        self._test1_grade = 0
        self._test2_grade = 0
        self._final_exam_grade = 0
        self._final_average = 0

    def add_quiz_grade(self, grade):
        self._quiz_grades.append(grade)

    def set_test1_grade(self, grade):
        self._test1_grade = grade

    def set_test2_grade(self, grade):
        self._test2_grade = grade

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
        quiz_weight = 0.15
        test1_weight = 0.25
        test2_weight = 0.25
        final_exam_weight = 0.35

        quiz_average = sum(self._quiz_grades) / len(self._quiz_grades) if self._quiz_grades else 0

        final_average = (
            quiz_average * quiz_weight +
            self._test1_grade * test1_weight +
            self._test2_grade * test2_weight +
            self._final_exam_grade * final_exam_weight
        )

        return final_average