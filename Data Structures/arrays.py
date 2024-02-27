# arrays
# An array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together. This makes it easier to calculate the position of each element by simply adding an offset to a base value, i.e., the memory location of the first element of the array (generally denoted by the name of the array). The base value is index 0 and the difference between the two indexes is the offset.

# to use arrays in python we have to import the array module

from array import array

listExample = [1,2,3,4,5] #this is a list , if we want to make it an arrayy we have to do the following

arraysOfNumbers = array("i", [1,2,3,4,5]) #this is an array of integers , the i is the typecode of the array, we can also use the typecode of the array as follows

#https://docs.python.org/3/library/array.html

print(arraysOfNumbers) #prints array('i', [1, 2, 3, 4, 5])


#we can use the same pop , remove  add methods on the array as we use on the list
