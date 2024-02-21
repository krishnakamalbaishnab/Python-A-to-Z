message = "a" # this is a global variable


def greet_user():
    # """Display a simple greeting."""
    global message # this is a global variable , this will modify the global variable
    message = "b" # this is a local variable

greet_user()


print(message) # this will print b