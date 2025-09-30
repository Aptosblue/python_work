motorcycles = []

motorcycles.append('honda') #insert list item to the end of list
motorcycles.append('yamaha')
motorcycles.append('suzuki')

motorcycles.insert(1, 'ducati') #insert listitem into specific position

print(motorcycles)

del motorcycles[1] #delete specific list item at specified position
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

popped_motorcycle = motorcycles.pop() #delete item from list and store it inside of a value for future use
print(motorcycles)
print(popped_motorcycle)

print(f'The last motorcycle I owned was a {popped_motorcycle.title()}.') #using the removed list item that has been stored for use in f string
first_motorcycle = motorcycles.pop(0)
print(f'The first motorcycle I owned was a {first_motorcycle.title()}.')
print(motorcycles)
motorcycles.remove('honda') #remove specific list item when you know the value for it
print(motorcycles)
motorcycles.insert(0, 'ducati')
motorcycles.insert(1, 'honda')
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f'\nA {too_expensive.title()} is too expensive for me.')
motorcycles.append('ducati')
motorcycles.append('ducati')
print(motorcycles)


motorcycles = [n for n in motorcycles if n != too_expensive]


print(motorcycles)



