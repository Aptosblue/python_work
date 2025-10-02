squares = [value**2 for value in range(1,11)] #list comprehension, a 'for' loop that automatically appends to the list
print(squares)

for value in range(1, 21):
    print(value)

all_numbers = []
for value in range(1, 1000001):
    all_numbers.append(value)

print(min(all_numbers))
print(max(all_numbers))
print(sum(all_numbers))

odd_numbers = []
for value in range(1,20,2):
    odd_numbers.append(value)
    print(value)

threes = []
for value in range(3,31,3):
    threes.append(value)
    print(value)

cubes = []
for value in range(1, 11):
    cubes.append(value**3)

for cube in cubes:
    print(cube)

cubes = [value**3 for value in range(1,11)]
print(cubes)
