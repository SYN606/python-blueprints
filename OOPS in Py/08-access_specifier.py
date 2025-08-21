"""
===========================================
      Access Specifiers in Python OOP
===========================================

Unlike some other languages, Python does not enforce access modifiers 
strictly, but it uses naming conventions:

1. Public Variables
   - Accessible from anywhere (inside/outside class).
   - No special prefix.

2. Protected Variables
   - Defined with a single underscore: _var
   - Intended to be used within the class and its subclasses.
   - Still accessible from outside (just a convention).

3. Private Variables
   - Defined with double underscore: __var
   - Name-mangled to prevent direct access from outside.
   - Accessible only within the class (but can still be accessed using _ClassName__var).
"""

# -------------------------------
# Base Class (Dad)
# -------------------------------
class Dad:
    __basketball = 1   # private variable

    def show_private(self):
        return f"Dad's private basketball skill = {self.__basketball}"


# -------------------------------
# Derived Class (Son)
# -------------------------------
class Son(Dad):
    _dance = 1   # protected variable

    def is_dance(self):
        return f"Yes, I dance {self._dance} time(s)."


# -------------------------------
# Further Derived Class (GrandSon)
# -------------------------------
class GrandSon(Son):
    dance = 6   # public variable

    def is_dance(self):
        return f"I am GrandSon and I dance {self.dance} time(s)."


# -------------------------------
# Demonstration
# -------------------------------
ayush = Dad()
ram = Son()
shyam = GrandSon()

# Public Variable
print("Public Variable (GrandSon):", shyam.dance)

# Protected Variable (Accessible but should be used carefully)
print("Protected Variable (Son):", ram._dance)

# Private Variable (Direct access fails)
# print(ayush.__basketball)   # ❌ AttributeError

# Access private variable via method
print("Private Variable (via method):", ayush.show_private())

# Access private variable using name mangling
print("Private Variable (via name mangling):", ayush._Dad__basketball)

"""
💡 Key Notes:
- Public: Accessible anywhere.
- Protected (_var): Convention → should only be used inside class & subclasses.
- Private (__var): Name-mangled → can’t be accessed directly, 
  but can be accessed using _ClassName__var.
"""
