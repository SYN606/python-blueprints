"""
===========================================
                Inheritance
===========================================

🔹 Inheritance → The mechanism that allows a class (child/derived class) 
                 to use the properties and methods of another class (parent/base class).

Benefits:
1. Promotes **code reusability**.
2. Establishes a hierarchical relationship between classes.
3. Child classes can **extend or override** parent functionality.

Types of Inheritance (in Python):
- Single Inheritance → Child inherits from one parent.
- Multiple Inheritance → Child inherits from multiple parents.
- Multilevel Inheritance → Child inherits from a parent, which itself inherits from another.
- Hierarchical Inheritance → Multiple children inherit from the same parent.
- Hybrid Inheritance → Combination of above types.
"""

# -------------------------------
# Parent Class
# -------------------------------
class Employee:
    num_of_leaves = 5 

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def print_details(self):
        return f"Name: {self.name}, Salary: {self.salary}, Role: {self.role}"

    @classmethod 
    def change_leaves(cls, new_leaves):
        cls.num_of_leaves = new_leaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod 
    def print_good(string):
        print("This is good " + string)


# -------------------------------
# Child Class (Single Inheritance)
# -------------------------------
class Programmer(Employee):
    def __init__(self, name, salary, role, languages):
        # Reuse parent constructor
        super().__init__(name, salary, role)
        # Add child-specific attribute
        self.languages = languages

    def print_prog(self):
        return (f"Programmer Name: {self.name}, Salary: {self.salary}, "
                f"Role: {self.role}, Languages: {', '.join(self.languages)}")


# -------------------------------
# Creating Objects
# -------------------------------
ram = Employee("Ram", 18000, "Instructor")
shyam = Employee("Shyam", 15000, "Clerk")
karan = Employee.from_dash("Karan-1500-Adviser")

ayush = Programmer("Ayush", 22000, "Programmer", ["Python", "C++"])


# -------------------------------
# Demonstration
# -------------------------------
print(ram.print_details())       # Parent method
print(ayush.print_prog())        # Child-specific method
print(ayush.print_details())     # Inherited parent method

# Static method and class method still available to child
ayush.print_good("Learning Inheritance")
Programmer.change_leaves(15)
print(f"Leaves after update: {Programmer.num_of_leaves}")


"""
💡 Key Notes:
1. Child class inherits all methods & attributes of the parent.
2. We can extend parent behavior by adding new attributes/methods.
3. We can override parent methods if we want different behavior in child.
"""
