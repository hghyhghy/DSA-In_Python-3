
# methods 

class Vector():

    x=0.0

    y=0.0


    # creating a method 

    def set(self,x,y):

        self.x=x

        self.y=y


def ofmain():

    # creating an object of the class Vector 

    myv=Vector()

    # accessing the elements by using  that object 

    myv.set(5,6)

    print("x", "is", myv.x , "y","is",myv.y)

ofmain()