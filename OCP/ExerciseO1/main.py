from OCP.ExerciseO1.classes.circle import Circle
from OCP.ExerciseO1.classes.rectangle import Rectangle
from OCP.ExerciseO1.classes.square import Square

if __name__ == "__main__":
    circle = Circle(5)
    print(circle.area())
    square = Square(5)
    print(square.area())
    rectangle = Rectangle(5,10)
    print(rectangle.area())


