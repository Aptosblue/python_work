cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.sort() #sort the order of the list in alphabetical order permanently, no way to return to original order
print(cars)

cars.sort(reverse=True) #sort the order of the list in reverse alphabetical order, no way to return to original order
print(cars)

cars.reverse() #flips the list, do not confuse with reverse alphabetical order, simply puts the last item as the first item, second to last - second...etc.
print(cars) #use reverse() again to return the list back to the original order

print('Here is the original list:')
print(cars)

print('Here is the sorted list:')
print(sorted(cars)) #temporarily sorts the list in alphabetical order, does not effect value of the list and all items in the list remain in the same position

print('Here is the original list again:')
print(cars) #Here we print the list again and we can see its the same as when we first printed the list before the sorted function

print(len(cars)) #counts the number of items in a list
cars.append('lexus') #lexus added to list
print(len(cars)) #the count has increased because we added a value to the list
