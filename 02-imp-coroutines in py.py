# ==============================
#   Coroutines in Python
# ==============================

"""
👉 Definition:
    - Coroutines are special functions in Python that can pause and resume 
      their execution at certain points.
    - They are more generalized than generators.
    - Unlike normal functions, coroutines can consume values with `send()` 
      as well as produce values with `yield`.

👉 Key Difference from Generators:
    - Generators produce data (using yield).
    - Coroutines consume data (using yield and send).

👉 Why use Coroutines?
    - Useful for tasks where you need to handle streams of data
      without restarting the function each time.
    - Commonly used in cooperative multitasking, event handling, 
      and asynchronous programming.

"""
import time

def Searcher():
    """
    Coroutine to search text inside a 'book'.
    First, it simulates loading a book (4 seconds delay).
    Then it keeps checking whether the given text exists in the book string.
    """
    book = "This is book."
    time.sleep(4)   # Simulating time-consuming task (e.g., loading resource)

    # Infinite loop that waits for input using yield
    while True:
        text = (yield)   # receives value from .send()
        if text in book:
            print(f"'{text}' is present in the book.")
        else:
            print(f"'{text}' is NOT present in the book.")


# ==============================
#   Example Usage
# ==============================
search = Searcher()
next(search)              # Prime the coroutine (required before first send)

search.send("Talwinder")  # Searching text not in book
input("Press any key...") # Keeps coroutine alive
search.send("is")         # Searching text that exists
