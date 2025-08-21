# Polymorphism in Object-Oriented Programming (OOP)

![OOP](https://img.shields.io/badge/OOP-Concept-blue) 
![Principle](https://img.shields.io/badge/Principle-Polymorphism-purple) 
![Python](https://img.shields.io/badge/Language-Python-green)

---

## 🔎 What is Polymorphism?
Polymorphism is the ability of an object to take on **multiple forms**.  
It allows methods or operators to behave differently based on the **object or data type** they are working with.  

In simple terms:  
👉 *The same function name can perform different tasks depending on the object that calls it.*

---

## ⚡ Types of Polymorphism

### 1. **Compile-time Polymorphism** (Method Overloading)  
- Same method name with **different parameter lists**.  
- Not natively supported in Python, but can be mimicked using default arguments or `*args`.

### 2. **Run-time Polymorphism** (Method Overriding)  
- A **child class** redefines a method from its **parent class**.  
- The version of the method that gets called depends on the object instance.

---

## 🐍 Example in Python

```python
# Example of Method Overriding (Run-time Polymorphism)

class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Different objects, same method name
animals = [Dog(), Cat(), Animal()]

for a in animals:
    print(a.speak())
