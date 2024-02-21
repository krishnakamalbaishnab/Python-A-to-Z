def multipleArguments(**args): # **args is a dictionary , when we use double asterisk then it means that we are passing a dictionary and we can pass any number of arguments
    print(args)


multipleArguments(name="Krishna", age=21, address="India") # here we are passing the dictionary as the argument 


# we can also use the double asterisk to pass the dictionary as the argument

def multipleArguments(**args): # **args is a dictionary , when we use double asterisk then it means that we are passing a dictionary and we can pass any number of arguments

    print(args["name"])

multipleArguments(name="Krishna", age=21, address="India") # here we are passing the dictionary as the argument