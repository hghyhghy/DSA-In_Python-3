

# python program tof reversal algorithm of array rotation

# creating a function 

def ofreverse(a,n):

    c=(a[n:]+a[:n])

    return c

a=[2,1,3,4,1,5]

n=1

print(ofreverse(a,n))