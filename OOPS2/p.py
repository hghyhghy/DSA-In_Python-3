

# polymorphism


class Bird:

    def intro(self):
        
        print("Mot of the birds can fly")

    def flight(self):

        print("But some of them dont")

class sparrow(Bird): # class sparrow inheriting bird

    def intro(self):
        
        print("Sparrow can fly")

class Ostrich(Bird):

    def intro(self):
        
        print("Ostrich can not fly")


# creating objects to this class

bird=Bird()

spr=sparrow()

ostr=Ostrich()

bird.intro()

bird.flight()

spr.intro()

spr.flight()

ostr.intro()

ostr.flight()


