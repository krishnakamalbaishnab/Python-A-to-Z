# example of finally block

# Path: Python-A-to-Z/Exceptions/try_exceptions.py

try:
    age = int(input("Enter your age: "))
    print("You are {} years old".format(age))
except ValueError:
    print("You did not enter a valid age")
finally:
    print("Thank you for using our application")
#In this example, the finally block will always be executed whether an exception is raised or not.
#The finally block is often used to release external resources such as files or network connections.
#In the example above, the finally block is used to close the file that was opened in the try block.
#If an exception is raised, the finally block will still be executed before the program terminates.
#This is useful for releasing resources that are no longer needed.
#The finally block is optional and can be omitted if it is not needed.
#The finally block is often used to release external resources such as files or network connections.