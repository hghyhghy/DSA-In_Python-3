

class Person:

    def __init__(self,name,company):

        self.name=name

        self.company=company


    def show(self):

        print("Hello my name is ", self.name ,"And I am working in",self.company," ") 

#creating objects 

obj=Person("Subham","Accenture")

obj.show()
    