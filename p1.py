

# accessing the values of dictionaires using loops 

# creating a dictionary 

d1={5:"Geeks ",6:"For",7:"Geeks"}


print("The  original dictionary is ")

print(d1)

print(f"The key values from the dictionary {d1} is ")

for i in d1:

    print(i,d1[i])

# accessing the valus using items() 

d={1:"Subham",2:"Loves his",3:"Mom and",4:"Shreyoshi"}

print("The original dictionary is")

print(str(d))

#use of dict.itms() method

print("The key, values  are")

for key,value in d.items():

    print(key,value)



