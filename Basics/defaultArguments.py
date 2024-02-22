def increment(number, by=1):
    return number + by

# print(increment(2, 5))


# we can simply call the function without passing the second argument and it will take the default value of the second argument

print(increment(2, by=5))



# default parameters / or optional parameters

def increment(number, by=1):
    return number + by

print(increment(2,3)) # here we are passing the value of by as 3 so the output will be 5
# if you don't pass the parameter by then the default value of by will be 1
print(increment(2)) # here we are not passing the value of by so the output will be 3