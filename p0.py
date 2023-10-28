

# creating a dictionary from the list 

# creating an empty dictionary 

d={}

print("The empty dictionary is ")

print(d)

#creatting a list

l=[(1,"Subham"),(2,"Love  his MOM")]

print("The list is ")

print(l)

print("The dictionary from the list is ")

d=dict(l)

print(d)


# merging two dictionaries 

d1={5:"Geeks ",6:"For",7:"Geeks"}

print("The concatenated dictionaries are ")

d1.update({8:"Python"})

print(d1)

# merging two dictionaries using |= operator 

veg1={1:"carrot",2:"Brinjal"}

veg2={3:"Lady Finger",5:"Onion"}

print("The concatenated dictionary is  ")

veg1|=veg2

print(veg1)

