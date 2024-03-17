# #classes are blueprints for creating objects

# #object is an instance of a class

# #class : Human
# # Objects : John, Mary, Jack 

# class Point: #class name should be in pascal case , this is a convention , creatign a class
#     def draw(self): #what this line is doing is that it is defining a method inside a class , this method is called draw
#         print("draw") #this is the body of the method

# variablePoint = Point() #this is how we create an object of a class , this is called instantiation, vrriablePoint is an object of the class Point, and it is an instance of the class Point

# print(type(variablePoint)) #this will print the type of the object variablePoint



class Computer:

    def __init__(self, cpu,ram): #this is a constructor, it is a special method in python, it is called when we create an object of a class, it is used
        self.cpu = cpu #self is a reference to the current object, it is a reference to the object that is being created
        self.ram = ram  #this is how we define the properties of the object
        print("in init")

    def config(self): #this is a method of the class computer
        print("The Configuration is ", self.cpu, self.ram) #this is the body of the method

computer1 = Computer('i5',16) #this is how we create an object of a class
computer2 = Computer("Ryzen 5", '32Gb') #this is how we create an object of a class

#computer.config(computer1) #this is how we call a method of a class

# computer1.config() #this is another way how we call a method of a class


#print(type(computer1)) #this will print the type of the object computer1

computer1.config()
computer2.config()

#in the above example, we have created a class computer, and we have created an object of the class computer, and we have called the method of the class computer using the object computer1

#in the above example, we have created a class computer, and we have created an object of the class computer, and we have called the method of the class computer using the object computer1