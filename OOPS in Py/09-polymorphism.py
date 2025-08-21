"""
===========================================
            Polymorphism in Python
===========================================

Polymorphism → "One name, many forms"

It allows:
1. Methods in different classes to have the same name but different behavior.
2. Objects of different classes to be treated as objects of a common base class.

Types:
- Compile-time Polymorphism (Method Overloading) → Not directly supported in Python.
- Run-time Polymorphism (Method Overriding) → Commonly used in Python.
"""

# -------------------------------
# Example 1: Method Overriding
# -------------------------------
class Animal:
    def speak(self):
        return "Some generic sound"

class Dog(Animal):
    def speak(self):   # overriding parent method
        return "Woof!"

class Cat(Animal):
    def speak(self):   # overriding parent method
        return "Meow!"


# -------------------------------
# Example 2: Same method name, different behavior
# -------------------------------
class Bird:
    def fly(self):
        return "Some birds can fly."

class Penguin(Bird):
    def fly(self):   # overriding parent method
        return "Penguins cannot fly, they swim instead."


# -------------------------------
# Demonstration of Polymorphism
# -------------------------------
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.speak())   # Same method name → different output

print()

birds = [Bird(), Penguin()]
for bird in birds:
    print(bird.fly())       # Same method name → different behavior


"""
💡 Key Notes:
1. Polymorphism allows the same method name to behave differently 
   depending on the object calling it.
2. Achieved in Python mainly via **method overriding**.
3. Useful for building flexible and extensible systems.
"""
