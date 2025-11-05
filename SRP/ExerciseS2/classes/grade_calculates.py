from SRP.ExerciseS2.classes.student import Student

class GradeCalculates:
    @staticmethod
    def calculating_averages(grades: Student):
        return sum(grades.grades) // len(grades.grades)