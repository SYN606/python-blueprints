"""
=====================================
        Functions & Docstrings
=====================================

🔹 Functions:
    - Functions are reusable blocks of code.
    - They take input (parameters), perform some logic,
      and return a result.

🔹 Docstrings:
    - Docstrings (Documentation Strings) are written inside triple quotes .
    - They describe what the function/class/module does.
    - Can be accessed using `.__doc__` attribute.
"""

# ---------------------------------------------------
# Example 1: Function with Return
# ---------------------------------------------------
def avg(a, b):
    """Return the average of two numbers."""
    average = (a + b) / 2
    return average


v = avg(5, 7)
print("Average is:", v)  # Output: Average is: 6.0


# ---------------------------------------------------
# Example 2: Function with Docstring
# ---------------------------------------------------
def add(x, y):
    """This function adds two numbers and returns the result."""
    return x + y


n = add(3, 6)
print("Sum is:", n)  # Output: Sum is: 9


# ---------------------------------------------------
# Printing Docstring
# ---------------------------------------------------
print("\nDocstring for `add` function:")
print(add.__doc__)  # Output: This function adds two numbers and returns the result.


"""
💡 Key Notes:
1. Use `return` if you want to use the function’s output later.
   - If you don’t use `return`, Python returns `None` by default.
2. Docstrings make your code more readable and maintainable.
3. Tools like `help(add)` also show docstrings, which helps in large projects.
"""
