from .main import Student

class EnglishStudent(Student):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name, "English")
        self._term_paper_grade = 0
        self._midterm_grade = 0
        self._final_exam_grade = 0
        self._final_average = 0

    def set_term_paper_grade(self, grade):
        self._term_paper_grade = grade

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
        term_paper_weight = 0.25
        midterm_weight = 0.35
        final_exam_weight = 0.4

        final_average = (
            self._term_paper_grade * term_paper_weight +
            self._midterm_grade * midterm_weight +
            self._final_exam_grade * final_exam_weight
        )

        return final_average