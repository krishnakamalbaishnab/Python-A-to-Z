#classes are blueprints for creating objects

#object is an instance of a class

#class : Human
# Objects : John, Mary, Jack 

class Point: #class name should be in pascal case , this is a convention , creatign a class
    def draw(self): #what this line is doing is that it is defining a method inside a class , this method is called draw
        print("draw") #this is the body of the method

variablePoint = Point() #this is how we create an object of a class , this is called instantiation, vrriablePoint is an object of the class Point, and it is an instance of the class Point

print(type(variablePoint)) #this will print the type of the object variablePoint

