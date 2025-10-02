for value in range(1,6): #Range starts at the first number you provide and ends at the last number
    print(value) # Because it ends at the last number, it will never print the last number. Meaning it's exclusive

#Giving range(6) only one argument will result in it counting from 0 and ending a 5 (exclusive of 6)
#When using range() and your output is off, try adjusting the values by 1

numbers = list(range(1,6)) #list() can be used to create a list from a range of numbers using range() as an argument
print(numbers) #Numbers will print in list format, not individually

[]