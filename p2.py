

# class with attribute 

class Dog():

    attr1="Mammal"

    #instance attribute 

    def __init__(self,name):

        self.name=name


# driver codw

# creating the attributes 

Rodger=Dog("Rodger")

Tommy=Dog("Tommy")

# accessing the class attributes 


print("Rodger is a", format(Rodger.__class__.attr1))

print("Tommy is a", format(Rodger.__class__.attr1))

# accessing the names 

print("My name is ", format(Rodger.name))

print("My name is ", format(Tommy.name))
 
 
