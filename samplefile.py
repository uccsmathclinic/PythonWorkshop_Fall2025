nb1= 12
nb2 = 45.67

print("nb1 is", nb1, end="\n\n\n")


# this is an example of unpacking

v=[23,45,66]

a,b,c = v # Unpacking
print(a,b,c)

v=[23,45,66,67,55,33]

a,b,c,*rest = v  # Unpacking

print(a,b,c,rest)

v=[23,45,66,67,55,33]

first, *rest, last  = v  # Unpacking
print(first, last,rest)

first= v[0]
last=v[-1]
rest=v[1:-1] # A slice (slice operator)
print(first, last,rest)
