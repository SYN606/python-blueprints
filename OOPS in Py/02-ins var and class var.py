"""
===========================================
   Instance Variables vs Class Variables
===========================================

🔹 Instance Variable → Belongs to a specific object (unique per object).  
🔹 Class Variable → Shared among all objects of the class.  

💡 Important:
- If we try to change a class variable using an object, 
  Python creates a new instance variable instead of modifying the class variable.
"""


# -------------------------------
# Defining a Class
# -------------------------------
class Employee:
    # Class Variable (shared by all instances)
    num_of_leaves = 5


# -------------------------------
# Creating Objects (Instances)
# -------------------------------
ram = Employee()
ram.name = "Ram"
ram.salary = 18000
ram.role = "Instructor"

shyam = Employee()
shyam.name = "Shyam"
shyam.salary = 15000
shyam.role = "Clerk"

# -------------------------------
# Accessing Instance Variables
# -------------------------------
print(f"Name: {ram.name}, Salary: {ram.salary}, Role: {ram.role}")
print(f"Name: {shyam.name}, Salary: {shyam.salary}, Role: {shyam.role}")

# -------------------------------
# Accessing Class Variable
# -------------------------------
print(f"Leaves allowed (via class): {Employee.num_of_leaves}")
print(f"Leaves allowed (via object): {ram.num_of_leaves}")

# If we change via class → it changes for all objects
Employee.num_of_leaves = 10
print(f"Updated leaves (via class): {Employee.num_of_leaves}")

# -------------------------------
# What if we try to change via object?
# -------------------------------
shyam.num_of_leaves = 7  # Creates a NEW instance variable (doesn't affect class variable)

print(f"Shyam's leaves (instance variable): {shyam.num_of_leaves}")
print(f"Employee class leaves (still unchanged): {Employee.num_of_leaves}")
print(f"Ram's leaves (still sees class variable): {ram.num_of_leaves}")

# -------------------------------
# Inspecting Class Dictionary
# -------------------------------
print("\nClass Dictionary (Employee.__dict__):")
print(Employee.__dict__)
