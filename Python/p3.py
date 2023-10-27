

# creating an empty dictionary

Dict={}

print("The empty dictionary is ")

print(Dict)

# adding  elements to the dict

Dict[0]="Subham"

Dict[1]="Loves"

Dict[2]="Shreyoshi"

Dict[3]=1

print("The dictionary after adding four elements ")

print(Dict)

# adding a set of values to a single key 

Dict["Value_sets"]=2,3,4

print("The dictionary after adding value sets elements are")

print(Dict)

#updating existing keys value

Dict[3]="And His Mom"

print("After updating the dictionary  ")

print(Dict)

# adding a nested dictionary


Dict[5]={"Nested":{"1":"life","2":"Is Large"}}

print("Adding the nested key")

print(Dict)
