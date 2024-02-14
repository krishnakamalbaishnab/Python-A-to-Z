# defining a function

def greet_user():
    # """Display a simple greeting."""
    print("Hello!")
greet_user()


# now we will pass a parameter to the function

def greet_user(username):
    # """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('krishna kamal baishnab') 


# difference between argumenst and parameters.. from he above code the username is a parameter and the value we pass to the function is called argument . so krishna kamal baishnab is the argument