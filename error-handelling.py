"""
=====================================
        Error Handling in Python
=====================================

Errors can occur at runtime (e.g., invalid input, missing files, division by zero).  
To prevent the program from crashing, we use `try-except` blocks.
"""

# Taking user input
num1 = input("Enter a number: ")
num2 = input("Enter a number: ")

try:
    # Try to run this code
    result = int(num1) + int(num2)
    print("The sum of two numbers is:", result)

except Exception as e:
    # If error occurs, handle it gracefully
    print("An error occurred:", e)

print("✅ This line will always run, even if an error happened above.")

"""
💡 Key Notes:
- try:     Code that might cause an error.
- except:  Code that runs if an error occurs.
- Exception: A built-in Python class that catches almost all errors.

Without try-except, the program would crash at runtime.
With try-except, the program continues smoothly after handling the error.
"""

# ------------------------------------
# Example: Handling Specific Exceptions
# ------------------------------------
try:
    num = int(input("Enter a number: "))
    print("10 divided by your number is:", 10 / num)

except ValueError:
    print("❌ Invalid input! Please enter a number.")

except ZeroDivisionError:
    print("❌ Division by zero is not allowed.")

except Exception as e:
    print("⚠️ Unexpected error:", e)

print("Program finished safely.")
