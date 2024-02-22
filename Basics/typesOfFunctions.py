
# there are two typeq of functions in python

# 1. Built-in functions
# 2. User-defined functions

# Built-in functions are those functions that are already defined in python and we can use them directly.
# for example: print(), input(), len(), type(), etc.

# User-defined functions are those functions that we define ourselves.

# defining a function

def greet_user():
    # """Display a simple greeting."""
    print("Hello!")

greet_user()

# now we will pass a parameter to the function

def greet_user(username):

    print(f"Hello, {username.title()}!")

greet_user('krishna kamal baishnab')



# a fucntons does two things

#  it returns a value
#  it does not return a value
