"""
===========================================
        Abstract Base Classes (ABC)
===========================================

🔹 Why use Abstract Base Classes?
    - When multiple classes share common functionality,
      we can enforce a common method structure in a base class.
    - ABCs ensure that derived classes MUST implement certain methods.

🔹 Key Points:
    1. We use Python’s built-in `abc` module.
    2. `ABC` is the base class for defining Abstract Base Classes.
    3. `@abstractmethod` decorator marks methods that 
       MUST be implemented by subclasses.
    4. Objects CANNOT be created directly from an abstract class.
    5. Abstract methods act like a "contract" that child classes must follow.
"""

# Importing Abstract Base Class tools
from abc import ABC, abstractmethod


# -------------------------------
# Abstract Base Class
# -------------------------------
class Shape(ABC):

    @abstractmethod
    def print_area(self):
        """
        Abstract Method:
        Must be implemented in derived classes.
        """
        pass


# -------------------------------
# Concrete Subclass: Rectangle
# -------------------------------
class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def print_area(self):
        """
        Overriding abstract method.
        """
        return self.length * self.breadth


# -------------------------------
# Concrete Subclass: Circle
# -------------------------------
class Circle(Shape):
    type = "Circle"
    sides = 0

    def __init__(self, radius):
        self.radius = radius

    def print_area(self):
        """
        Overriding abstract method.
        Formula: πr²
        """
        from math import pi
        return pi * (self.radius**2)


# -------------------------------
# Demonstration
# -------------------------------
# rect1 = Shape()  # ❌ ERROR: Cannot instantiate abstract class
rect1 = Rectangle(5, 6)
circle1 = Circle(4)

print("Rectangle Area:", rect1.print_area())
print("Circle Area:", circle1.print_area())
"""
💡 Key Notes:
1. Shape is an Abstract Base Class — cannot create objects from it.
2. Rectangle and Circle inherit Shape, so they MUST implement print_area().
3. If a child class does not implement the abstract method, 
   Python will throw an error.
4. Abstract Base Classes help enforce consistency across related classes.
"""
