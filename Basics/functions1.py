# # defining a function

# def greet_user():
#     # """Display a simple greeting."""
#     print("Hello!")
# greet_user()


# # now we will pass a parameter to the function

# def greet_user(username):
#     # """Display a simple greeting."""
#     print(f"Hello, {username.title()}!")

# greet_user('krishna kamal baishnab') 


# difference between argumenst and parameters.. from he above code the username is a parameter and the value we pass to the function is called argument . so krishna kamal baishnab is the argument
list = ['krishna', 'kamal', 'baishnab']

def loopThroughList(myList):
    for item in myList:
        print(item)

loopThroughList(list)



def addNumbers(a,b):
    print(a+b)

addNumbers(2,3)


# in programming we have two types of functions

# 1. function that performs a task
# 2. function that returns a value


def increement(number ,by):
    return number + by

result = (increement(2,3))  #if this line seems confuding for people who is reading this code, what we can do is that we can write the increment function in this way [increement(4, by=3)]

print(result)