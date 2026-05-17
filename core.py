#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 19:30:26 2026

@author: navjyot
"""
# 1. print and comment

"""

Single line comment start with #
Used to explain functions, classes, or big blocks.

"""

print("Hello, World")
print("My name is Python")

# ------------------------------------------------
# 2. variable and data types
# ------------------------------------------------

name = "Alice"
age = 25
height = 5.6
is_cool = True
nothing = None

print(type(name))
print(type(age))
print(type(height))
print(type(is_cool))

# ------------------------------------------------
# 3. Input From User
# -------------------------------------------------

user_name = input("Enter your name: ")
print("Hello", user_name)

# Converting input to number:
# print("Hello,", user_name)

# age = int(input("Enter your age:"))
# print("Next year you will be:", age + 1)

# ------------------------------------------------------
# 4,Operators
# -----------------------------------------------------
print(10 + 3)
print(10 - 2)
print(10 * 3)
print(10 // 3)
print(10 % 3)
print(2 ** 3)

# Comparison (return True/False)
print(5 > 3)
print(5 < 3)
print(5 == 5)
print(5 != 3)
print(5 >= 5)

# -------Logical operator
print(True and False)
print(True or False)
print(not True)

# Assignment Shorthand
x = 10
x += 5
x -= 4
x *= 2
x //= 4
print(x)

# ---------------------------
# 5.strings
# ---------------------------

s = "Hello, python"

print(len(s))
print(s.upper())
print(s.lower())
print(s.replace("Python", "world"))
print(s.split(" , "))
print(s[0])
print(s[-1])
print(s[0:5])
print("s.strip()")
print("python" in s)
print("python" in s)

# f strings (best way to format strins)
name = "Bob"
age = 30
print(f"my name is {name} and I am {age} years old.")
print(f"Next year I will be there {age + 1}")

# Strings method
print("hello ".strip())
print("hello world". ttitle())
print("hello.center(11, "-")")
print(",".join(["a", "b", "c"]))

# 6. if / elif / else
# make decision based on conditions

marks = 75

if marks >= 90:
    print("Grade: A+")

elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60
print("Grade: C")
else:
    print("Grade: F - Study Harder!")

# one liner (Ternary)
result = "Pass" if marks >= 50 "fail"
print(result)  # pass

# 7. loops

for i in range(5):
    print(i, end=" ")
 print()
 
for i in range(1, 11):
    print(i, end = " ")
print()

# Loops over a list

fruits = ["apple", "banana", "cherry"]
for fruits in fruits:
    print(f"I love {fruits}!")
    
# loop with index using enumerate

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruits}")



# While loop: use when condition controls the loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1
    
    
# break, continue, Pass

for i in range(10):
    if i == 3:
        continue
    if i == 7:
        break
    print(i, end = " ")
print()

# pass placeholder, does nothing
for i  in range(3):
    pass 

# 8 .list

num = [10, 20, 30, 40, 50]

print(nums[0])
print(nums[-1])
print(nums[1:4])

nums.append(60)
nums.insert(0, 5)
nums.remove(30)
popped = nums.pop()
print(nums)

nums.sort()
nums.sort(reverse = True)
print(sorted(nums))

print(len(nums))
print(sum(nums))
print(min(nums))
print(max(nums))
print(20 in nums)

# List comprehension (short + powerful!)

squares = [x ** 2 for x in range(1, 6)]
print(squares) 

evens = [x for x in range(20) if x % 2 == 0]
print(evens)

# Tuples

points = (10, 20)
colors = ("red", "green", "blue")

print(colors[0])
print(len(colors))
print("red" in colors)

# tuple unpacking
x, y = points
print(f"x = {x}, y = {y}")

# Single item tuple need trailing comma
single  = (42,)
print(type(single))

# 10.sets

my_set = {1, 2, 3, 4, 5}
my_set.add(6)
my_set.discard(3)
print(my_set)

a = {1,2,3,4,5}
b = {3,4,5,6}

print(a | b)
print(a & b)
print(a - b)
print(a ^ b)

# Dictionaries
# key value pairs. Like a real dictionary: word - meaning

person = {
    "name": "Alice",
    "age": 25,
    "city": "NYC"
    }

print(person["name"])
print(person.get("age"))
print(person.get("salary", 0))

person["email"] = "alicegmail.com"
person["age"] = 26
del person["city"]

print(person.keys())
print(person.values())
print(person.items())

# loop through dictionary
for key, value in person.items():
    print(f"{key}: {value}")
    
# Dict comprehension
squares = {x: x ** 2 for x in range(1, 6)}
print(squares)

# functions
# Resuable blocks of code

def greet(name):
    return f"Hello, {name]!"

print(greet ("Alice")
      
def power((3))
print(power(2, 10))

def min_max(number):
    return min(numbers), max(numbers)

low, high = min_max([5,1,9,3])
print(f"Min = {low}, Max = {high}")

# *args accepts any number of positional arguments

def total(*nums):
    return sum(nums)

print(total(1,2,3,4,5))

# kwargs - acceptsany number of keyboard arguments
def profile(**info):
    for k, v in info.items():
        print(f" {k}: {v}")
        
profile(name = "Bob", age = 30, city = "LA")

# Lambda (anonymous one - linear function)
squares = lambda x: x ** 2
add = lambda x, y: x + y
is_even = lambda x: x % 2 == 0

print(squares(5)) 
print(add(3, 4))
print(is_even(8))

# Lambda with map, filter, sorted
nums = [1,2,3,4,5,6]
doubled = list(map(lambda x: x % 2 == 0, nums))
print(doubled)
print(evens)

# 13 Scope local and global variable

total_score = 100

def add_bonus():
    print(total_score)
    total_score += 10
    
add_bonus()
print(total_score)

# 14 Exception handling (try / except)

# Handle errors gracefully so the program doesnt crash

try:
    num = int("abc")
    result = 10 / 0
except ValueError as e:
    print(f"valueError: {e}")
except ZeroDivisionError:
    print("cant divide by zero")
except Exception as e:
    print(f"Unexpected error: {e}")
    
else:
    print("No error occured!")
finally:
    print("This always runs!")

# raise your own exeption
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return f"Age is {age}"

try:
    print(check_age(-5))
except ValueError as e:
    print(e)

# File handling

# write to a file
with open("sample.txt", "w") as f:
    f.write("Hello, File! \n")
    f.write("Second line.\n")
    
# Read line by line
with open("sample.txt", "a") as f:
    for line in f:
        print(line.strip())
    
    
# Read entire file
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)
    
# Append to file
with open("sample.txt", "a") as f:
    f.write("Appended line.\n")
    
# Read all line into a list
with open("sample.txt", "r") as f:
    lines = f.readlines()
    print(lines)
    
# (OOP) Object Oriented programming

# class = Blueprint object = Real thing built from blueprint
class Animal:
    # Class variable (shared by all objects)
    kingdom = "Animalia"
    
    # Constructor (__init__) sets up the object
    def __init__(self, name, sound):
        self.name = name # instance variable
        self.sound = sound
        
    # method (function inside class)
    def speak(self):
        return f"{self.name} says {self.sound}"
    
    def __str__(self):
        return f"Animal({self.name})" # print-friendly
    
    def __str__(self):
        return f"Animal({self.name})" # print - friendly

        
dog = Animal("Dog", "Woof")
cat = Animal("Cat", "Meow")

print(dog.speak())
print(cat.speak())
print(dog.kingdom)
print(str(dog))


# Inheritance (child class gets parents features)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, breed):
        self.breed = breed
        
    def fetch(self):
        return f"{self.name} fetch the ball"
    
    def speak(self):
        return f"{self.name} barks loudly:"
    
my_dog = Dog("Rex", "Labrador")
print(my_dog.speak())
print(my_dog.fetch())
print(my_dog.kingdom())


# Encapsulation
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance # private (name mangled)
        
    def deposit(self, amount):
        if amount > 0:
            self.balance = balance += amount
            
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.balance -= amount
        else :
            print("Insufficient funds")
            
    def get_balanced(self):
        return self.__balance
    
acc = BankAccount("Alice", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.get_balanced())
#print(acc.__balanced)
        



# --- Encapsulation (hide data with _ or __) ---
class BankAccount:
    def __init__(self, owner, balance):
        self.owner    = owner
        self.__balance = balance    # private (name mangled)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.__balance


acc = BankAccount("Alice", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.get_balance())   # 1300
# print(acc.__balance)     # AttributeError! (private)


# 17. module and import

import math
import random
import datetime

print(math.pi)
print(math.ceil(4.2))
print(math.sqrt(16))
print(math.floor(4.9))

print(random.randint(1, 10))
print(random.choice)(["a", "b","c"]))
nums = [1,2,3,4,5]
random.shuffle(nums)
print(nums)

now = datetime.datetime.now()
print(now)
print(now.strftime("%Y-%m-%d %H: %M: %S"))

# 18 List 

# list Comprehension
cubes = [x ** 3 for x in range (1, 6)]

# Dict comprehension
word_len = {word: len(word) for word in ["apple", "hi", "banana"]}

# Set comprehension
unique_sq = {x ** 2 for x in [-2, -1, 0, 1, 2]}

print(cubes)
print(word_len)
print(unique_sq)

# 19 Generators (Memory Efficient loops)

# generate value one at a time (does not store all in memory)

def countdown(n):
    while n > 0:
        yield n
        n -= 1
for num in countdown(5):
    print(num, end = "5"):
print()

# 20 Generator expression (like list comprehension but lazy)
gen = (x ** 2 for x in range(10))
print(next(gen)) 
print(next(gen))
print(next(gen))

# Decorators (Advanced Functions)
# A function that wraps another function to add behavior

def log_it(func):
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}....")
        result = func(*args, **kwargs)
        print(f"Done! Result: {result}")
        return result
    return wrapper

@log_it()
def add(a, b):
    return a + b

add(3, 5)

# 21. *args and **kwargs (deep dive)

def show_info(*args, **kwargs):
    print("Positional:", args)
    prnt("Keyword:", kwargs)
    
show_info(1,2,3, name = "Alice", age: 25)
# Positional: (1,2,3)
# Keyword: {"name": "Alice", "age: 25}

# 22. Useful Built In function

nums = [3,1,4,1,5,9,2,6]

print(len(nums))
print(sum(nums))
print(min(nums))
print(max(nums))
print(sorted(nums))
print(list(reversed(nums)))

print(list(range(5)))
print(list(enumerate(["a","b","c"])))
print(list(zip([1,2,3], ["a","b","c"])))

print(abs(-7))
print(round(3.14159, 2))
print(isinstances(5, int))
print(type(3.14))

# 23. String Formatting

name, score = "Alice", 98.5

# 1. f-string (best & modern)
print(f"name: {name}, Score: {score:. 1.f}")

# 2. .format()
print("Name: {}, Score: %.1f".format(name, score))

# 3. % Operators (old style)
print("Name: %s, Score: %.1f" % (name, score))

# walrus operator := (Python 3.8+)
# Assign AND use a variable in the same expression

data = [1,2,3,4,5,6,7,8,9,10]

if (n := len(data)) > 5:
    print(f"List is long ({n} items)!")
    
# Useful in while loop
import random
while (num := random.randint(1, 10)) != 7:
    print(f"Got {num}, trying again....")
print(f"Finally got 7")

# 25 Quick Reference Cheat sheet

"""
Data types:
    str, int, float, bool, None,
    list, tuple, set, dict

Loops:
    for x in iterable:
    while condition:
    break / continue / pass

Functions:
    def name(params): return value
    lambda x: expression
    *args - tuple of positionals
    **kwargs - dict of keywords
    
OOP:
    class Name:
        def __init__(self):...
        def method(self):...
        Inheritance: class child(parent)
        super().__init__()
        
Error Handling:
    try / except else / finally
    raise Exception("msg")
    
Files:
    with open("file.txt", "r/w/a") as f:
        f.read()
        
Comprehension:
    [x for x in list if condition]
    {k: v for k, v in dict.item()}
    {x for x in list}
    
Useful modules:
    math, random, datatime, os,
    sys, json, re, collections
    
print("\n core python complete yu are ready to build amazing things")

"""














