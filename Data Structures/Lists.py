letters = ['a', 'b', 'c', 'd']

listOfLists = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] #listoflist is called as an matrix

print(listOfLists) #prints 2

# suppose we want to make a list of zeros we can do it in the following way

zeros = [0]*5
print(zeros) #prints [0, 0, 0, 0, 0]

# list concatenation

listA = [1,2,3,4]
listB = ['a','b','c']

listC = listA + listB

print(listC) #prints [1, 2, 3, 4, 'a', 'b', 'c']


# creating a list using the range function  

listD = list(range(20))
print(listD) #prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# Accessing the elements of the list

print(letters[0]) #prints a
print(letters[1]) #prints b


# finding the length of the list

print(len(letters)) #prints 4

# finding the index of the element in the list

print(letters.index('a')) #prints 0

# finding the count of the element in the list

print(letters.count('a')) #prints 1