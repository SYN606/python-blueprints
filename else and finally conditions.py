"""
    Python Exception Handling (try, except, else, finally)

    👉 Exception handling in Python allows us to handle errors gracefully 
       instead of crashing the program.

    Syntax:
        try:
            # Code that may raise an error
        except <ErrorType>:
            # Code to handle the error
        else:
            # Code that runs if no exception occurs
        finally:
            # Code that always runs (cleanup tasks)

    ✅ Explanation of blocks:
        - try     : The block of code where exceptions may occur.
        - except  : Handles the exception if it occurs.
        - else    : Runs only if no exception was raised inside try.
        - finally : Runs no matter what (used for cleanup, closing files, etc.).
"""

# Example: Reading a file with exception handling
try:
    with open("file.txt") as f:
        data = f.readlines()
    print("File contents:", data)

except FileNotFoundError as e:
    print("Error: File not found ->", e)

except PermissionError as e:
    print("Error: Permission denied ->", e)

except Exception as e:
    print("General error occurred:", e)

else:
    print("✅ File read successfully (no exception occurred).")

finally:
    print("🔒 Important Task: Closing resources or cleanup.")
