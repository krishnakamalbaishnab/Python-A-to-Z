# # Stack Data Structure
# # STACK HAS THE LIFO BEHAVIOUR -> LAST IN FIRST OUT

# # Stack is a linear data structure which follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out).


# # example, when we open a website on browser, and go inside tge main website and keep going insdide two three more links of the website, 


# # now let's see the example of stack using list

# browsingSites = []

# browsingSites.append(1)
# browsingSites.append(2)
# browsingSites.append(3)
# browsingSites.append(4)

# # what the above the coding is doing is that we are adding the websites to the stack

# print(browsingSites) #prints [1, 2, 3, 4]

# # now suppose we want to go back to the previous website, we can do it in the following way so once we click the back button the last website will be removed from the stack
# # so it will be removed in the following way , in general it will be back from the 4 to 3 and so on

# browsingSites.pop() #removes the last website from the stack

# print(browsingSites) #prints [1, 2, 3]

# last = browsingSites.pop(-1) #removes the last website from the stack and stores it in the last variable
# print(last) #prints 3/ the last website

# # once we reach the end of the browsing we can clear the stack in the following way and the back buton will be disabled

# # so let's check it how it works 
# browsingSites[-1] # returns the last website from the stack

# if not browsingSites:
#     print("disable") #prints disable
