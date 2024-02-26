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


# filter function

# suppose we want to filter the products whose price is greater than 10, we can do it in the following way  

filtered = filter(lambda item: item[1] > 10, items2)

print(list(filtered)) #prints [('product3', 12)]

# list comprehensions

# suppose we want to make a list of the prices of the products whose price is greater than 10, we can do it in the following way

filtered2 = [item for item in items2 if item[1] > 10]

print(filtered2) #prints [('product3', 12)]

# zip function

list1 = [1,2,3]
list2 = [10,20,30]

print(list(zip(list1,list2))) #prints [(1, 10), (2, 20), (3, 30)]


# Stack Data Structure
# STACK HAS THE LIFO BEHAVIOUR -> LAST IN FIRST OUT

# Stack is a linear data structure which follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out).


# example, when we open a website on browser, and go inside tge main website and keep going insdide two three more links of the website, 


# now let's see the example of stack using list

browsingSites = []

browsingSites.append(1)
browsingSites.append(2)
browsingSites.append(3)
browsingSites.append(4)

# what the above the coding is doing is that we are adding the websites to the stack

print(browsingSites) #prints [1, 2, 3, 4]

# now suppose we want to go back to the previous website, we can do it in the following way so once we click the back button the last website will be removed from the stack
# so it will be removed in the following way , in general it will be back from the 4 to 3 and so on

browsingSites.pop() #removes the last website from the stack

print(browsingSites) #prints [1, 2, 3]

last = browsingSites.pop(-1) #removes the last website from the stack and stores it in the last variable
print(last) #prints 3/ the last website

# once we reach the end of the browsing we can clear the stack in the following way and the back buton will be disabled

# so let's check it how it works 
browsingSites[-1] # returns the last website from the stack

if not browsingSites:
    print("disable") #prints disable



# Queue Data Structure

# Queue is a linear structure which follows a particular order in which the operations are performed. The order is First In First Out (FIFO). A good example of a queue is any queue of consumers for a resource where the consumer that came first is served first. The difference between stacks and queues is in removing. In a stack we remove the item the most recently added; in a queue, we remove the item the least recently added.

# QUEUE HAS THE FIFO BEHAVIOUR -> FIRST IN FIRST OUT
# example 
# when we send a message to someone on whatsapp, the message goes to the end of the queue and the person at the start of the queue gets the message first

# now let's see the example of queue using list

from collections import  deque #importing the deque class from the collections module

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.popleft() #removes the first element from the queue
print(queue) #prints deque([1, 2, 3, 4])

if not queue:
    print("empty") #prints empty

# what this above code is doing is that we are adding the elements to the queue and then removing the first element from the queue and then checking if the queue is empty or not

# swap two variables

x= 10
y= 20

z = x
x = y
y =z


print(x) #prints 10
print(y) #prints 10