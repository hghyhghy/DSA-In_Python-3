
# constructor in python 

class Addition:

    first=0

    second=0

    answer=0

    def __init__(self,first,second):

        self.first=first

        self.second=second

    def display(self):

        print("First number is ","=", str(self.first))

        print("Second number is ","=", str(self.second))

        print("Answer is ","=", str(self.answer))


    def calculate(self):

        self.answer=self.first+self.second


obj1=Addition(20,2)

obj1.calculate()

obj1.display()

obj=Addition(2000,2000)

obj.calculate()

obj.display()
 