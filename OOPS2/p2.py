

# classes and instance variables 

# creating a dog 

class Dog:

    #  class variable 

    animal="Dog"

    def  __init__(self,breed,color):

        self.breed=breed

        self.color=color


# creating the objects 

Rodger=Dog("Pug","Brown")

Tini=Dog("Bulldog","Black")

print("Rodger Details")

print("Rodger is a ",Rodger.animal)

print("Rodger is a ",Rodger.breed)

print("Rodger's color is   ",Rodger.color)

print("Tini Details")


print("Tini is a ",Tini.animal)

print("Tini is a ",Tini.breed)

print("Tinis's color is   ",Tini.color)
 

 




        