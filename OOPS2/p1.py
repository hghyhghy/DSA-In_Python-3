

# the __str__ method 

class Animal:

    attr="Dog"

    def __init__(self,name):

        self.name=name
    

    # the __str__ method 

    def __str__(self):

         return ( f"My dogs name is  { self.name}")


myanimal=Animal("Kutta")

print(myanimal)