"""
    Python *args and **kwargs

    |> In Python, *args and **kwargs allow functions to accept a variable number of arguments.

    1. *args
       - Collects extra positional arguments into a tuple.
       - Useful when you don't know beforehand how many arguments will be passed.
    
    2. **kwargs
       - Collects extra keyword arguments into a dictionary.
       - Useful when you want to pass named arguments without fixing them in advance.

    ✅ Syntax order in function parameters:
        (normal_args, *args, **kwargs)

    👉 Both *args and **kwargs are optional.
"""

# Example without *args
# def func_print_name(a, b, c, d):
#     print(a, b, c, d)
# func_print_name("Lmao", "Lmau", "Lol", "Loml")


# Example with *args and **kwargs
def func_name_1(normal, *args, **kwargs):
    print("Normal argument:", normal, "\n")

    print("Positional arguments (*args):")
    for item in args:
        print(item)

    print("\nKeyword arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} is used for {value}")


# Passing values
name = ["bachha 1", "bachha 2", "bachha 3", "bachha 4"]

normal = "I am a normal function argument"

kw = {
    "Python": "Development",
    "C language": "Core Programming",
    "Java": "Game Development",
    "C++": "Game Development"
}

# Function call with *args and **kwargs
func_name_1(normal, *name, **kw)
