
# inheritance 

class Pet:

    def __init__(self,name,age):

        self.name=name

        self.age=age


# inheriting the class Pet by a class Cat
    
class Cat(Pet):

    def __init__(self, name, age):
       
       # inheriting the superclass function 
       #by using super()  keyword 
         
        super().__init__(name, age)


# creating the driver code 

def ofmain():

    #creating the object in class Pet

    thepet=Pet("thePet",2)

    mycat=Cat("myCat",1)

    # the isinstance() is the keyword is used to check 

    # wheather the class is inherited from other or not 

    print("Is Tini is a cat", str(isinstance(mycat,Cat)))

    print("Is thepet is a pet", str(isinstance(thepet,Pet)))

