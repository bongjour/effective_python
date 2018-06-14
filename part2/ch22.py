import collections

grades = []
grades.append((95, 0.45))

total = sum(score * weight for score, weight in grades)
total_weight = sum(weight for _, weight in grades)

print(total)

Grade = collections.namedtuple('Grade', ('score', 'weight'))


class Subject(object):
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score=score, weight=weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight = grade.weight

        return total / total_weight


class Student(object):
    def __init__(self):
        self._subjects = {}

    def subject(self, name) -> Subject:
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]

    def average_grade(self) -> float:
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count


class Gradebook(object):
    def __init__(self):
        self._students = {}

    def student(self, name) -> Student:
        if name not in self._students:
            self._students[name] = Student()
        return self._students[name]


book: Gradebook = Gradebook()
student: Student = book.student('dante')
math: Subject = student.subject('Math')
math.report_grade(80, 0.10)

print(student.average_grade())
