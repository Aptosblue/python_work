my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:] # You can copy a list by using an empty slice
print(friends_foods)

#to prove each list will now be different, we will add an item to each and print

my_foods.append('cannoli')
friends_foods.append('ice cream')

print('My favorite foods are: ')
for food in my_foods:
    print(food.title())

print('My friends favorite foods are: ')
for food in friends_foods:
    print(food.title())