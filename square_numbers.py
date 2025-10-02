square_numbers = []
for value in range(1,11): #Selects range from 1-10 inclusive
    square = value ** 2 #Squares the number. For idiots, it multiplies the number by itself.
    square_numbers.append(square) #adds the squared number to the list

print(square_numbers) #Output = [1, 4, 9 , 16, 25, 36, 49, 64, 81, 100]

for value in range(1,11):
    square_numbers.append(value**2) #We can also write it this way to simplify it
    pass
    #Here we simply square the argument inside the append method
