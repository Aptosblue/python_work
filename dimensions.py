dimensions = (200, 50) # Tuples are lists that you cannot change, Python calls this "immutable"
print(dimensions[0])
print(dimensions[1]) #If we try to change this to a different value, we will get a TypeError

my_t = (3,) # If we wanted to make a tuple with one value, we need to unclude a trailing comma

#Although we cannot change a tuple like we can a list. If the values in a tuple need to change, we can assign new values to the varible itself, see below
print('Original Dimensions:')
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100) #writing over the original value
print('\nNew Dimensions:')
for dimension in dimensions:
    print(dimension)

# Tuples are useful when you want to keep values static throughout the program