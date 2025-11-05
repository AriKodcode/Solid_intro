from SRP.ExerciseS2.classes.student import Student
from SRP.ExerciseS2.classes.grade_calculates import GradeCalculates

if __name__ == "__main__":
    student = Student("Ari",[100,95,90])
    sum_grades = GradeCalculates
    print(sum_grades.calculating_averages(student))