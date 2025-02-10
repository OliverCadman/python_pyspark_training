"""Section 1: Variables & Basic Operations"""
"""Variables are containers for storing data values"""

# Challenge 1: Store and Print a Variable
# Declare a variable called name and assign it your name. Then, print it.

# my_name = "Evelyn"
# print(f'My name is {my_name}')

# Challenge 2: Simple Math Operations
# Declare two numbers and print their sum, difference, and product.

num1 = 5
num2 = 2.0
total = num1 + num2

# print(f'The sum of {num1} + {num2} = {total}')
# print(f'The sum of {num1} + {num2} = {num1 + num2}')

"""If you want to specify the data type of a variable, this can be done with casting"""
# input1 = float(input("Enter a value from 0 to 1: "))
# input2 = float(input("Enter a value from 0 to 1: "))
# total = input1 + input2
# print(total)


# Challenge 3: Swap Two Variables
# Swap the values of two variables without using a third variable.

# Initial values of variables
a = 5
b = 10

# print("before the swap")
# print(f'a={a}, b={b}')

# print("after the swap")
# a, b = b, a
# print(f'a={a}, b={b}')


"""Section 2: Loops & Iteration"""
# Challenge 4: Use a for loop to print numbers from 1 to 10.
# for number in range(1, 11):
    # print(number)

# Challenge 5: Multiplication Table
# Ask the user for a number and print its multiplication table up to 10.
# number = int(input("Enter a value: "))

# for x in range(1, 11):
#     result = number * x
#     print(f'Multiplication table for {number}: {result}')
 

# Challenge 6: Count Down from 10 to 1
# Use a while loop to count down from 10 to 1 and then print "Happy New Year, Welcome to 01/01/2025!!" You can import both time and
# datetime module to make the count down more interesting and simulate the count down for new years!

import time
import datetime

# count = 10
# start_time = datetime.datetime(2024, 12, 31, 23, 59, 50)
# print(start_time)

# while count > 0:
#     current_time = start_time + datetime.timedelta(seconds=(10 - count))
#     print(f'{current_time} - Countdown: {count}')
#     count -= 1
#     time.sleep(1)

# print('Happy new year!!')

"""Code Modularity in Python 🧩

Code modularity refers to breaking a program into smaller, reusable, and 
independent modules to improve readability, maintainability, and reusability. 
In Python, modularity is achieved through functions, classes, modules, and packages"""

"""Section 3: Functions & User Input"""

# Challenge 7: Greeting Function
# Write a function called greet() that takes a name as an argument and prints "Hello, [name]!".
def greet(name):
    print(f'my name is {name}')

# greet("Evelyn")

# Challenge 8: Sum of First N Numbers
# Write a function sum_n(n) that returns the sum of all numbers from 1 to n.
def sum_n(i):
    return sum(range(1, i + 1))

# try: 
#     n = int(input("Enter a number: "))
#     print(f'the sum of the first {n} numbers is {sum_n(n)}')
# except:
#     print("Error, Enter a valid number")

# Challenge 9: Define the function to convert Celsius to Fahrenheit (celsius * 9/5) + 32


# Challenge 10: Simple Login System
""" Define a function login_system that:
    1) Takes a username and password as inputs.
    2) Validates them against stored values (e.g., a hardcoded username and password).
    3) Allows the user to attempt logging in multiple times until successful or they choose to quit"""



"""Python Task: Create the core logic for a calculator application, with a focus on modularity and re-usable code"""
