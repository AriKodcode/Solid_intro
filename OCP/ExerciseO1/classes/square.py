from OCP.ExerciseO1.classes.shape import Shape
class Square(Shape):

    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a * self.a
