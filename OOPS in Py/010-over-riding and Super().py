"""
===========================================
      Method / Variable Overriding & super()
===========================================

🔹 Overriding
   - When a child class defines a variable or method 
     with the same name as its parent, it replaces (overrides) the parent’s version.

🔹 super()
   - A built-in function used inside a child class 
     to call the constructor or methods of the parent class.
   - Ensures parent initialization happens before child-specific initialization.
"""

# -------------------------------
# Parent Class
# -------------------------------
class A:
    classvar = "I am a class variable in class A"

    def __init__(self):
        self.var = "I am inside Class A's constructor"
        self.classvar = "Instance variable in Class A"
        self.special = "Special from A"


# -------------------------------
# Child Class
# -------------------------------
class B(A):
    classvar_2 = "I am class B"

    def __init__(self):
        # Calls Parent constructor first
        super().__init__()  

        # Overriding instance variables
        self.var = "I am inside Class B's constructor"
        self.classvar = "Instance variable in Class B"


# -------------------------------
# Demonstration
# -------------------------------
a = A()
b = B()

print("From Class A instance:")
print("var:", a.var)
print("classvar:", a.classvar)
print("special:", a.special)

print("\nFrom Class B instance (after overriding):")
print("var:", b.var)                # overridden
print("classvar:", b.classvar)      # overridden
print("special:", b.special)        # inherited from A
print("classvar_2:", b.classvar_2)  # unique to B


"""
💡 Key Notes:
1. Child class `B` overrides `var` and `classvar` defined in Parent `A`.
2. `special` is inherited from Parent `A` because it's not overridden.
3. `super()` ensures that `A`'s constructor runs first, 
   so attributes like `special` are properly initialized.
4. Without `super()`, child `B` would not inherit the initialization from `A`.
"""
