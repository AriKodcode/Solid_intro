from OCP.ExerciseO1.classes.shape import Shape

class Circle(Shape):
    def __init__(self,r):
        self.r = r


    def area(self):
        return (self.r * 2) * 3.14
