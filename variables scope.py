# -----------------------------
# Global and Local Variables
# -----------------------------

l = 10   # Global Variable

def func(n):
    # l = 5   # Local variable (if uncommented, it shadows the global variable)
    
    global l  # Tells Python: use the global 'l' instead of creating a local one
    print("Value of l (global):", l)

    l = 20   # Now we can modify the global variable
    print("I have printed:", n)

func("This is me")
print("Updated value of l (global):", l)


"""
📌 Key Notes:
------------------------------------------
1. Global Variable:
   - Declared outside all functions.
   - Can be accessed inside functions, but cannot be modified unless declared with `global`.

2. Local Variable:
   - Declared inside a function.
   - Only accessible inside that function.
   - If a local variable has the same name as a global variable, it shadows the global one.

3. The 'global' keyword:
   - Allows modifying a global variable inside a function.

🔎 Rule: Python first looks for variables in local scope, if not found, then searches in global scope.
"""
