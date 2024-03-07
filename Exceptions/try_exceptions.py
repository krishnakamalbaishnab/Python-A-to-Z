try:
    age = int(input("Enter your age: "))
    print("You are {} years old".format(age))
except ValueError:
    print("You did not enter a valid age")


#so what this code is going to do is to ask the user to enter their age and then it will print out the age.
#If the user enters a string instead of an integer, the code will raise a ValueError and print out the message "You did not enter a valid age".

# Multiple except blocks

# Path: Python-A-to-Z/Exceptions/try_exceptions.py

try:
    age = int(input("Enter your age: "))
    print("You are {} years old".format(age))
except ValueError:
    print("You did not enter a valid age")
except ZeroDivisionError:
    print("You cannot divide by zero")

#In this example, we have added a second except block to handle the ZeroDivisionError exception.

# Handling multiple exceptions in one except block

# Path: Python-A-to-Z/Exceptions/try_exceptions.py

try:
    age = int(input("Enter your age: "))
    print("You are {} years old".format(age))
except (ValueError, ZeroDivisionError): # we can also use a tuple to handle multiple exceptions in one except block
    print("You did not enter a valid age")
