"""
===========================================
            Multiple Inheritance
===========================================

🔹 Multiple Inheritance → When a class inherits from more than one parent class.

👉 Syntax:
class Child(Parent1, Parent2, ...):
    pass

⚡ Important:
- If two parents have methods with the same name, Python resolves it using the **MRO (Method Resolution Order)**.
- You can check MRO with: ClassName.mro()
"""


# -------------------------------
# Parent Class 1
# -------------------------------
class Employee:
    num_of_leaves = 5

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def print_details(self):
        return f"Employee → Name: {self.name}, Salary: {self.salary}, Role: {self.role}"

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
# Parent Class 2
# -------------------------------
class Player:
    no_of_games = 4

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def print_game(self):
        return f"Player → Name: {self.name}, Game: {self.game}"


# -------------------------------
# Child Class (Multiple Inheritance)
# -------------------------------
class CoolProgrammer(Employee, Player):
    language = "Python"

    def __init__(self, name, salary, role, *game):
        Employee.__init__(self, name, salary, role)
        Player.__init__(self, name, game)

    def print_language(self):
        return f"Favorite Language: {self.language}"

    def print_all_details(self):
        emp = self.print_details()
        game_info = f"Player → Name: {self.name}, Game: {self.game}" if self.game else "No game assigned"
        lang = self.print_language()
        return f"{emp}\n{game_info}\n{lang}"


# -------------------------------
# Creating Objects
# -------------------------------
ram = Employee("Ram", 18000, "Instructor")
kabir = Player("Kabir", "Cricket")

# Multiple inheritance object
# rahim = CoolProgrammer("Rahim", 25000, "Programmer")

# -------------------------------
# Demonstration
# -------------------------------
print(ram.print_details())
print(kabir.print_game())

rahim = CoolProgrammer("Rahim", 25000, "Developer")
print(rahim.print_details())
print(rahim.print_all_details())

# -------------------------------
# Method Resolution Order (MRO)
# -------------------------------
print("\nMRO for CoolProgrammer:")
print(CoolProgrammer.mro())
