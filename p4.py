

# python inheritance problem 

class Person:

    def __init__(self,name,idnumber):

        self.name=name

        self.idnumber=idnumber

    def display(self):

        print(self.name)

        print(self.idnumber)

    def details(self):

        print("The name of the employee is ", format(self.name))

        print("The idnumber of the employee is ", format(self.idnumber))

# child class


class Employee(Person):  # inheriting the elements of the  parent class 

    def __init__(self, name, idnumber,salary,post):

        self.salary=salary

        self.post=post
    
        Person.__init__(self,name,idnumber)

    def details(self):

        print("My name is {}".format(self.name))

        print("My idnumber is {}".format(self.idnumber))

        print("My salary is {}".format(self.salary))

        print("My post is {}".format(self.post))


a=Employee("My Mom","100","0","Housewife")

a.display()

a.details()






    