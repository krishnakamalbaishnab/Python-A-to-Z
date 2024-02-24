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


i = 0
while i < 3:
    print(i)
    i += 1
else:
    print(0)

# accessing items in a list

listOne = ["b","b","c","d"]

print(listOne[0]) #prints b

# accessing items in a list using negative index

print(listOne[-1]) #prints d

# accessing items in a list using slicing

print(listOne[0:2]) #prints ['b', 'b']

# accessing items in a list using slicing

print(listOne[1:]) #prints ['b', 'c', 'd']

# accessing items in a list using slicing

print(listOne[:2]) #prints ['b', 'b']

customList = list(range(20)) # creates a list of 20 elements

print(customList) #prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

#now if we want to access the elements from 3 to 10 we can do it in the following way

print(customList[3:11]) #prints [3, 4, 5, 6, 7, 8, 9, 10]

# if we want to access the elements from 3 to 10 with a step of 2 we can do it in the following way

print(customList[3:11:2]) #prints [3, 5, 7, 9]

# if we want to access the elements from 3 to 10 with a step of 2 in reverse order we can do it in the following way

print(customList[10:2:-2]) #prints [10, 8, 6, 4]


# list unpacking or destructuring

myList = [1,2,3,4,5,6,7,8,9,10]

print(myList) #prints [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# now if we want to unpack the list into multiple pieces , what we can do is as follows

# suppose we want the first second and third element in the list

first,second,third, *rest = myList

print(first) #prints 1
print(second) #prints 2
print(third) #prints 3
print(rest) #prints [4, 5, 6, 7, 8, 9, 10]


# looping through the list

for i in enumerate(myList):
    print(i) #prints 1,2,3,4,5,6,7,8,9,10


# adding for removing a element from the list

myList.append(11) #adds 11 to the end of the list , we use append when we want to add an    element to the end of the list

myList.insert(0,0) #adds 0 to the beginning of the list , we use insert when we want to add an element at a specific position in the list


print(myList) #prints [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


# removing an element from the list

myList.pop() #removes the last element from the list


print(myList) #prints [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

myList.pop(0) #removes the first element from the list

print(myList) #prints [2, 3, 4, 5, 6, 7, 8, 9, 10]

myList.remove(3) #removes the first occurence of the element from the list

print(myList) #prints [2, 4, 5, 6, 7, 8, 9, 10]

# reversing the list

myList.reverse()

myList.clear() #removes all the elements from the list

del myList[0:3] #deletes the list

print(myList) #prints []



# finding items ina list

myList2 = ["a","b","c","d","a"]


print(myList2.index("a")) #prints 0


# what if we want to check if a element is present in the list or not

if "a" in myList2:
    print("yes") #prints yes

# if we want to check the occurance of the element in the list

print(myList2.count("a")) #prints 2


# sorting the list


items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12)
]


def sort_item(item):
    return item[1]

items.sort(key=sort_item)

print(items) #prints [('product2', 9), ('product1', 10), ('product3', 12)]

# explaination of the above code

# In this code, return item[1] is a part of the sort_item function. Let's break down the code:

# The items list contains tuples where each tuple has two elements: the name of a product and its corresponding price.
# The sort_item function is defined to take an item (which is a tuple) as input and return the second element of that tuple (index 1), which in this case is the price.
# The sort method is called on the items list with the key parameter set to the sort_item function. This means that the sort method will use the values returned by the sort_item function to determine the order of sorting.


# using lambda function to sort the list

items.sort(key=lambda item: item[1])

print(items) #prints [('product2', 9), ('product1', 10), ('product3', 12)]



# map functiion

items2 = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12)
]

# now suppose we want to make a different list from the above list, imagine we only want the price of the prducts in a different list,so what we are gonns do is that

# we will use the map function to do this

# lets see how we can do this

prices = [] #declaring an empty list

for i in items2:
    prices.append(i[1]) #appending the prices of the products to the prices list , here i[1] is the price of the product i,e the second element of the tuple

print(prices) #prints [10, 9, 12]

# now lets see how we can do the same thing using the map function


usingMapPrice = map(lambda item: item[1], items2)

print(list(usingMapPrice)) #prints [10, 9, 12] 