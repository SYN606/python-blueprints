"""
===========================================
        Class Methods and Static Methods
===========================================

🔹 Instance Method (default)
   - Takes `self` as the first parameter.
   - Can access & modify instance variables.

🔹 Class Method (@classmethod)
   - Takes `cls` as the first parameter.
   - Works with the class itself, not just one object.
   - Can modify **class variables**.
   - Can also be used as an **alternative constructor**.

🔹 Static Method (@staticmethod)
   - Does not take `self` or `cls`.
   - Behaves like a normal function inside a class.
   - Used for utility/helper functions (not tied to class or object).
"""

# -------------------------------
# Defining a Class
# -------------------------------
class Employee:
    # Class Variable
    num_of_leaves = 5 

    # Constructor (__init__)
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    # Instance Method
    def print_details(self):
        return f"Name: {self.name}, Salary: {self.salary}, Role: {self.role}"

    # Class Method (modifies class variables)
    @classmethod
    def change_leaves(cls, new_leaves):
        cls.num_of_leaves = new_leaves

    # Alternative Constructor (class method)
    @classmethod
    def from_dash(cls, string):
        # "Karan-1500-Adviser" → ["Karan", "1500", "Adviser"]
        name, salary, role = string.split("-")
        return cls(name, int(salary), role)
        # OR shorter: return cls(*string.split("-"))

    # Static Method (utility function)
    @staticmethod
    def print_good(string):
        print("This is good " + string)


# -------------------------------
# Creating Objects
# -------------------------------
ram = Employee("Ram", 18000, "Instructor")
shyam = Employee("Shyam", 15000, "Clerk")

# Using Alternative Constructor
karan = Employee.from_dash("Karan-1500-Adviser")


# -------------------------------
# Demonstration
# -------------------------------
print(ram.print_details())      # Instance method
print(karan.print_details())    # Created using class method constructor

# Changing class variable using class method
Employee.change_leaves(25)
print(f"Leaves after update: {Employee.num_of_leaves}")

# Static method usage
Employee.print_good("OOP in Python")
karan.print_good("Static Method Example")

"""
💡 Key Notes:
1. Instance methods → use `self` → access object data.
2. Class methods → use `cls` → access/modify class-level data (shared by all).
3. Static methods → no `self` or `cls` → act as helper functions inside a class.
"""
