

# different dictionary methods in python

# creating a dictionary

d={1:"Subham",2:"Loves his",3:"Mom and",4:"Shreyoshi"}

#copying  element to another dict

d1=d.copy()

print("The newly copied element in the dictionary is ")

print(d1)

# get method

print(f"The first element of the dictionary {d1} is ")

print(d1.get(1))


# getting  elements by using items () method 

print(f"The items  of the dictionary {d1} is ")

print(d1.items())

# deleting element by using pop method 

print(f"Deleting the  last  element of the dictionary {d1} is ")

print(d1.pop(4))

#updating the elements of the dictionary by using update() 

print("The updated dictionary is ")

d1.update({4:"Shreyoshi"})

print(d1)

