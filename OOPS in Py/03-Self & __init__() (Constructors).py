"""
===========================================
        self and __init__ in Python OOP
===========================================

🔹 self → Represents the instance of the class (the object itself).
          - It is automatically passed when we call a method on an object.
          - It allows access to instance variables and methods of the class.

🔹 __init__ → A special method in Python classes called "constructor".
              - It runs automatically whenever a new object is created.
              - It initializes (assigns values to) instance variables.

💡 Together, they make it possible to set up object data cleanly 
   when the object is created.
"""


# -------------------------------
# Defining a Class with Constructor
# -------------------------------
class Employee:
    # Class Variable (shared among all objects)
    num_of_leaves = 5

    # Constructor (__init__)
    def __init__(self, name, salary, role):
        # Instance Variables (unique for each object)
        self.name = name
        self.salary = salary
        self.role = role

    # Instance Method
    def print_details(self):
        return f"Name: {self.name}, Salary: {self.salary}, Role: {self.role}"


# -------------------------------
# Creating Objects (Instances)
# -------------------------------
ram = Employee("Ram", 18000, "Instructor")
shyam = Employee("Shyam", 15000, "Clerk")

# -------------------------------
# Accessing Data
# -------------------------------
print(ram.print_details())
print(shyam.print_details())
"""
💡 Key Notes:
1. self:
   - Acts like "this" keyword in other languages (Java, C++).
   - Refers to the *current object* calling the method.
   - Example: ram.print_details() internally becomes Employee.print_details(ram).

2. __init__:
   - Called automatically when a new object is created.
   - Helps us initialize instance variables (so we don’t assign them manually each time).
   - Without __init__, we’d have to do:
        ram.name = "Ram"
        ram.salary = 18000
        ram.role = "Instructor"
"""
