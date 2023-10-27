

# accessing the elements of the  dictionary

# creating a dictionary first

d={1:"Hello",2:"Python","Bad":"How are you"}

# accessing the element using key

print("Accessing the element of dictionary by using key")

print(d[2])

# accessing the element using value

print("Accessing the element of dictionary by using value")

print(d["Bad"])
 

# accessing the elements by using get() method

print("The element of the dictionary by using get()  method is ")

print(d.get(1))


# accessing the element of the  nested dictionary

# creating a nested dictionary

d1={1:{2:"Subham"},3:{4:"And His Mom"}}

print("The element from the nested dictionary is ")

print(d1[3])

# deleting an  element by using del keyword 

del(d1[1])

print("After deleting the dictionary becomes")

print(d1)