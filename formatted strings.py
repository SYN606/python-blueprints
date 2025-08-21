"""
=====================================
        Formatted Strings in Python
=====================================

We often need to insert variables inside strings.
Python provides 3 main ways to do this:

1. %-formatting   (Old style)
2. str.format()   (Newer style)
3. f-strings      (Modern, Python 3.6+)
"""

# ---------------------------------------------------
# 1. %-Formatting (Old Style)
# ---------------------------------------------------
a = "this is a string"
b = 5
str1 = "The string is: %s %s" % (a, b)
print(str1)  # Output: The string is: this is a string 5

# ---------------------------------------------------
# 2. .format() Method (New Style)
# ---------------------------------------------------
str2 = "This is {} {}".format(a, b)
print(str2)  # Output: This is this is a string 5

# You can also use positional or named arguments:
str3 = "Hello {0}, your number is {1}".format("Ram", 101)
print(str3)  # Output: Hello Ram, your number is 101

str4 = "Hello {name}, your marks are {marks}".format(name="Shyam", marks=88)
print(str4)  # Output: Hello Shyam, your marks are 88

# ---------------------------------------------------
# 3. f-Strings (Modern, Best Practice )
# ---------------------------------------------------
str5 = f"This is {a} {b}"
print(str5)  # Output: This is this is a string 5

# f-strings can also evaluate expressions inside {}
x, y = 7, 3
print(f"The sum of {x} and {y} is {x + y}")  # Output: The sum of 7 and 3 is 10
"""
💡 Key Notes:
- %-formatting is old and rarely used now.
- .format() is powerful (supports reordering, named args).
- f-strings are the most recommended way:
    ✅ Cleaner
    ✅ Faster
    ✅ Can evaluate expressions directly
"""
