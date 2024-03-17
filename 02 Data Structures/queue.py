# # Queue Data Structure

# # Queue is a linear structure which follows a particular order in which the operations are performed. The order is First In First Out (FIFO). A good example of a queue is any queue of consumers for a resource where the consumer that came first is served first. The difference between stacks and queues is in removing. In a stack we remove the item the most recently added; in a queue, we remove the item the least recently added.

# # QUEUE HAS THE FIFO BEHAVIOUR -> FIRST IN FIRST OUT
# # example 
# # when we send a message to someone on whatsapp, the message goes to the end of the queue and the person at the start of the queue gets the message first

# # now let's see the example of queue using list

# from collections import  deque #importing the deque class from the collections module

# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.append(4)
# queue.popleft() #removes the first element from the queue
# print(queue) #prints deque([1, 2, 3, 4])

# if not queue:
#     print("empty") #prints empty

# # what this above code is doing is that we are adding the elements to the queue and then removing the first element from the queue and then checking if the queue is empty or not

# # swap two variables

# x= 10
# y= 20

# z = x
# x = y
# y =z


# print(x) #prints 10
# print(y) #prints 10
