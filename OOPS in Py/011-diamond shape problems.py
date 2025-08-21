"""
===========================================
        Diamond Shape Problem in OOP
===========================================

🔹 Diamond Shape Problem:
   - Occurs in multiple inheritance when a class inherits from two classes
     that both inherit from the same base class.
   - This creates ambiguity: which parent’s method should the child class use?

Example Shape:
       A
      / \
     B   C
      \ /
       D

⚡ Problem:
If both B and C override a method from A,
then D (which inherits from both B and C) may not know which one to call.

🔹 Solution in Python:
Python uses **MRO (Method Resolution Order)** to decide.
- MRO follows the C3 linearization algorithm.
- You can check it using: `ClassName.mro()`
"""

# -------------------------------
# Base Class
# -------------------------------
class A:
    def print_a(self):
        print("This is a method from Class A")


# -------------------------------
# First Child Classes
# -------------------------------
class B(A):
    # Uncomment to see overriding effect
    # def print_a(self):
    #     print("This is a method from Class B")
    pass


class C(A):
    # Uncomment to see overriding effect
    # def print_a(self):
    #     print("This is a method from Class C")
    pass


# -------------------------------
# Grandchild Class (Multiple Inheritance)
# -------------------------------
class D(B, C):  
    pass


# -------------------------------
# Demonstration
# -------------------------------
a = A()
b = B()
c = C()
d = D()

d.print_a()   # Which method gets called?

print("\nMRO for Class D:")
print(D.mro())
