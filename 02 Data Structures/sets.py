
# set

# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.

# setExample = {1,2,3,4,5}

# print(setExample) #prints {1, 2, 3, 4, 5}

# # we can also use the set function to create a set

# setExample2 = set([1,2,3,4,5])

# print(setExample2) #prints {1, 2, 3, 4, 5}

# we can not use indexing to access an set item

# we can perform the following operations on the set

# add
# update
# remove
# discard

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9}

print(set1| set2) #prints {1, 2, 3, 4, 5, 6, 7, 8, 9} #union of the two sets
print(set1 & set2) #prints {4, 5} #intersection of the two sets
print(set1 - set2) #prints {1, 2, 3} #difference of the two sets
print(set1 ^ set2) #prints {1, 2, 3, 6, 7, 8, 9} #symmetric difference of the two sets
