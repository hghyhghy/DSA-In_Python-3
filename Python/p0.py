

# finding the maximum element from the array 

# creating a function 

def ofmax(a,n): # taking two arguments 

    # initializing the max element 

    max=a[0]

    # using a for loop 

    for i in  range(1,n):

        if a[i]>max:
         
         max=a[i]

    return max


# creating the  array 

a=[1,6,3,99]

n=len(a)

print(f"The highest  element from the array {a} is ")

print(ofmax(a,n))


# approach 2

# using max

# creating a function

def ofmax1(a1):
   
   return max(a1)

a1=[12,3,44,3,2,1]

print(ofmax1(a1))