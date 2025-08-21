"""
===========================================
     Dunder Methods & Operator Overloading
===========================================

🔹 Dunder Methods:
   - Special methods in Python that start and end with `__` (double underscore).
   - They let us define how objects of a class behave with built-in functions
     and operators.
   - Example: `__init__`, `__str__`, `__repr__`, `__add__`, etc.

🔹 Operator Overloading:
   - Normally, operators (+, -, *, /, etc.) don’t work with user-defined classes.
   - By defining dunder methods, we can change how these operators behave 
     when used with objects.

🔹 Common Examples:
   - `__add__`      → `+`
   - `__sub__`      → `-`
   - `__mul__`      → `*`
   - `__truediv__`  → `/`
   - `__str__`      → `str(obj)` or `print(obj)`
   - `__repr__`     → `repr(obj)` (unambiguous representation)
"""


# -------------------------------
# Employee Class
# -------------------------------
class Employee:
    num_of_leaves = 5 

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    # Instance method
    def print_details(self):
        return f"The name of employee is {self.name}, salary is {self.salary} and role is {self.role}."
    
    # Class method
    @classmethod
    def change_leaves(cls, new_leaves):
        cls.num_of_leaves = new_leaves

    # Operator Overloading
    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    # String Representations
    def __repr__(self):
        """
        🔹 Used for debugging and developer-oriented representation.
        Should be unambiguous.
        """
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        """
        🔹 Used for user-friendly string representation.
        Called by print() and str().
        """
        return self.print_details()


# -------------------------------
# Demonstration
# -------------------------------
emp_1 = Employee("Ram", 18000, "Instructor")
emp_2 = Employee("Rohan", 11000, "Cleaner")

# Operator Overloading
print("Operator Overloading Examples:")
print("emp_1 + emp_2 =", emp_1 + emp_2)   # calls __add__
print("emp_1 / emp_2 =", emp_1 / emp_2)   # calls __truediv__

# String Representations
print("\nString Representation Examples:")
print("Using print(emp_1):", emp_1)       # calls __str__
print("Using repr(emp_1):", repr(emp_1))  # calls __repr__


"""
💡 Key Notes:
1. __add__ lets us add salaries directly (emp_1 + emp_2).
2. __truediv__ lets us divide salaries directly (emp_1 / emp_2).
3. __str__ gives a clean, user-friendly summary when printing objects.
4. __repr__ gives an official, unambiguous representation for debugging.
5. Operator overloading makes classes behave more like built-in types.
"""
