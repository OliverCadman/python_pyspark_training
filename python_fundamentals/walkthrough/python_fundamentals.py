"""Section 1: Variables & Basic Operations"""
"""Variables are containers for storing data values"""

# Challenge 1: Store and Print a Variable
# Declare a variable called name and assign it your name. Then, print it.

# name = "Evelyn"
# print(f'My name is {name}')

# Challenge 2: Simple Math Operations
# Declare two numbers and print their sum, difference, and product.

num1 = 5
num2 = 2.0
print(f'The sum of {num1} + {num2} is {num1 + num2}')
print(f'The difference of {num1} - {num2} is {num1 - num2}')
print(f'The product of {num1} * {num2} is {num1 * num2}')

"""If you want to specify the data type of a variable, this can be done with casting"""

# Challenge 3: Swap Two Variables
# Swap the values of two variables without using a third variable.

# Initial values of variables
a = 5
b = 10

# Output before swapping
print("Before swapping:")
print(f"a = {a}, b = {b}")

# Swap the values without a third variable
a, b = b, a

# Output after swapping
print("\nAfter swapping:")
print(f"a = {a}, b = {b}")

"""Section 2: Loops & Iteration"""
# Challenge 4: Use a for loop to print numbers from 1 to 10.

for number in range(1, 11):
    print(number)

# Challenge 5: Multiplication Table
# Ask the user for a number and print its multiplication table up to 10.

# Step 1: Ask the user for a number
number = int(input("Enter a number to generate its multiplication table: "))

# Step 2: Print the multiplication table up to 10
print(f"Multiplication table for {number}:")

for i in range(1, 13): 
    result = number * i
    print(f"{number} x {i} = {result}")

# Challenge 6: Count Down from 10 to 1
# Use a while loop to count down from 10 to 1 and then print "Blast Off!".

# Step 1: Initialize the countdown starting number
count = 10

# Step 2: Use a while loop to count down
while count > 0:
    print(count) 
    count -= 1

print("Happy New Year!!")

"""Code Modularity in Python 🧩

Code modularity refers to breaking a program into smaller, reusable, and 
independent modules to improve readability, maintainability, and reusability. 
In Python, modularity is achieved through functions, classes, modules, and packages"""

"""Section 3: Functions & User Input"""

# Challenge 7: Greeting Function
# Write a function called greet() that takes a name as an argument and prints "Hello, [name]!".

def greet(name):
    print(f'Hello, {name}')

greet("Evelyn")

# Challenge 8: Sum of First N Numbers
# Write a function sum_n(n) that returns the sum of all numbers from 1 to n.

# Step 1: Define the function to calculate the sum of numbers from 1 to n
def sum_n(n):
    return resultsum(range(1, n + 1))  # Using the built-in sum function with a range
    
# Step 2: Test the function
try:
    n = int(input("Enter a number: "))
    result = sum_n(n)
    print(f"The sum of the first {n} numbers is: {result}")
except ValueError:
    print("Error: Invalid value entered")

# Challenge 9: Define the function to convert Celsius to Fahrenheit (celsius * 9/5) + 32

# Challenge 10: Simple Login System
""" Define a function login_system that:
    1) Takes a username and password as inputs.
    2) Validates them against stored values (e.g., a hardcoded username and password).
    3) Allows the user to attempt logging in multiple times until successful or they choose to quit"""

# Step 1: Define the login function
def login_system():
    # Hardcoded valid username and password
    valid_username = "evelyn"
    valid_password = "password123"
    
    # Maximum number of attempts
    max_attempts = 3
    attempts = 0
    
    print("Welcome to the login system!")
    
    # Step 2: Loop until the user either logs in or runs out of attempts
    while attempts < max_attempts:
        # Get input from the user
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
        # Step 3: Validate the credentials
        if username == valid_username and password == valid_password:
            print("Login successful! Welcome, admin.")
            break 
        else:
            attempts += 1
            print(f"Invalid credentials. You have {max_attempts - attempts} attempt(s) left.")
            
        # If user exceeds maximum attempts
        if attempts == max_attempts:
            print("Too many failed attempts. Access denied.")

# Step 4: Call the function
# login_system()

"""Python Task: Create the core logic for a calculator application, with a focus on modularity and re-usable code"""
