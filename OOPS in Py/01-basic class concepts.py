"""
===========================================
   Introduction to Classes and Objects
===========================================

🔹 Class → A template / blueprint for creating objects.  
🔹 Object → An instance created from a class (based on the template).  

👉 Think of a class like a "form" and objects as "filled copies" of that form.
"""

# -------------------------------
# Defining a Basic Class
# -------------------------------
class Student:  
    # Convention: Class names should start with a Capital Letter
    pass


# -------------------------------
# Creating Objects from Class
# -------------------------------
student_1 = Student()   # object of Student class
student_2 = Student()   # another object


# -------------------------------
# Adding Instance Variables
# (unique to each object)
# -------------------------------
student_1.name = "Ram"
student_1.std = 9
student_1.section = "B"
student_1.subjects = ["Hindi", "English", "Math"]

student_2.name = "Shyam"
student_2.std = 10
student_2.section = "A"
student_2.subjects = ["Hindi", "English", "Math"]

"""
💡 Note:
- Variables inside objects are called **instance variables**.
- If variables are defined inside the class itself (not in objects),
  they are called **class variables** (shared across all objects).
"""

# -------------------------------
# Accessing Object Data
# -------------------------------
print(f"The name of student is {student_1.name} and the class is {student_1.std}")
print(f"The name of student is {student_2.name} and the class is {student_2.std}")
