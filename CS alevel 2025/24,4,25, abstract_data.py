from abc import ABC, abstractmethod

# Interface (Abstract Base Class)
class Shape(ABC):
    _count = 0  # Static\class variable to keep track of the number of shapes
    @abstractmethod
    def area(self):
        """Abstract method to calculate the area."""
        pass

    def display(self):
        """Virtual-like method with a default implementation."""
        print("This is a generic shape.")

    def identify(self):
        """Regular method (not virtual or abstract)."""
        print("It's a shape!")

    # @staticmethod
    def get_shape_count():
        """Static method to get the total number of shapes created."""
        return Shape._count

    def __init__(self):
        if not hasattr(Shape, '_count'):
            Shape._count = 0
        Shape._count += 1

# Concrete class implementing the Shape interface
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return 3.14159265359 * self.radius * self.radius

    def display(self):
        print(f"Circle with radius: {self.radius}")
        print(f"Area: {self.area()}")

# Another concrete class implementing the Shape interface
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def display(self):
        print(f"Rectangle with width: {self.width} and height: {self.height}")
        print(f"Area: {self.area()}")

# Calling static method directly from the class
print(f"Initial shape count: {Shape.get_shape_count()}")

# Creating instances of concrete classes
circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Shape count after creation: {Shape.get_shape_count()}")

# Polymorphism in action
shapes = [circle, rectangle]
for shape in shapes:
    print("\n--- Shape Information ---")
    print(f"Area: {shape.area()}") # Calls the specific area() method
    shape.display()                 # Calls the overridden display() method
    shape.identify()                # Calls the base class identify() method

# You cannot instantiate the abstract base class directly:
# abstract_shape = Shape() # This would raise a TypeError