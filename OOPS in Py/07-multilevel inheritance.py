"""
===========================================
           Multi-Level Inheritance
===========================================

🔹 Multi-level Inheritance → When a class inherits from a child class, 
   forming a "chain" of inheritance.

Example:
Dad → Son → GrandSon

⚡ Key Points:
1. Attributes & methods are passed down the chain.
2. If a child redefines (overrides) a method or variable, it replaces the parent’s version.
3. Python searches for attributes/methods using **MRO (Method Resolution Order)**.
"""

# -------------------------------
# Parent Class
# -------------------------------
class Dad:
    basketball = 1   # class variable (all Dads play basketball by default)


# -------------------------------
# Child Class (inherits Dad)
# -------------------------------
class Son(Dad):
    dance = 1

    def is_dance(self):
        return f"Yes, I dance {self.dance} time(s)."


# -------------------------------
# Grandchild Class (inherits Son)
# -------------------------------
class GrandSon(Son):
    guitar = 1
    dance = 6   # overrides dance from Son

    # overrides method from Son
    def is_dance(self):
        return f"I am GrandSon and I dance {self.dance} time(s)."


# -------------------------------
# Creating Objects
# -------------------------------
ayush = Dad()
ram = Son()
shyam = GrandSon()

# -------------------------------
# Demonstration
# -------------------------------
print("Dad has basketball skill:", ayush.basketball)

print("Son inherits basketball from Dad:", ram.basketball)
print("Son dancing ability:", ram.is_dance())

print("GrandSon inherits basketball from Dad:", shyam.basketball)
print("GrandSon dancing ability (overridden):", shyam.is_dance())

# -------------------------------
# Method Resolution Order (MRO)
# -------------------------------
print("\nMRO for GrandSon:")
print(GrandSon.mro())
