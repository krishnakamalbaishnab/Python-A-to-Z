def fizzBuzzAlgorithm(input):
        if input % 3 == 0 and input % 5 == 0:
            print("FizzBuzz")
        elif input % 3 == 0:
            print("Fizz")
        elif input % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzBuzzAlgorithm(45)



# another way to solve the problem

def fizzBuzzAlgorithm(input):
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input

print(fizzBuzzAlgorithm(45))
