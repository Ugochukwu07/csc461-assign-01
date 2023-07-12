class Student:
    def __init__(self, first_name, last_name, course):
        self._first_name = first_name
        self._last_name = last_name
        self._course = course
        self.scores = []

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_course(self):
        return self._course

    def add_score(self, score):
        self.scores.append(score)

    def get_average_score(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0

    def __str__(self):
        return f"Student ID: {self.student_id}\nName: {self.first_name} {self.last_name}"
