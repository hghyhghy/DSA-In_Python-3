

# to find the sum of the array 

# creating an array first

# creating a function


def ofsum(a):

    # initializing a variable with  zero

    sum=0

    # using a for loop 

    for i in a:

        sum+=i

    return sum

# creating the array

a=[10,3,12]

print(f"The sum of the numbers in the array{a} is ")

# calling the function

print(ofsum(a))


#  approach2 

# by using built in function sum()

a1=[1,2,3,4,5]

temp=sum(a1)

print(f"The sum of the numbers from the array{a1} is ")

print(temp)

