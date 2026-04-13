class Shape:
    def __init__(self, colour):
        self.colour = colour
        
    def howManySides(self):
        print("I am a general shape.")

class Rectangle(Shape):
    def __init__(self, colour):
        super().__init__(colour)
        
    def howManySides(self):
        print(f"I am a {self.colour} rectangle. I have 4 sides.")

class Circle(Shape):
    def __init__(self, colour):
        super().__init__(colour)
        
    def howManySides(self):
        print(f"I am a {self.colour} circle. I have 0 sides.")


my_rectangle = Rectangle("Red")
my_rectangle.howManySides()

my_circle = Circle("Blue")
my_circle.howManySides()
