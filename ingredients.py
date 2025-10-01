ingredients = ['egg', 'milk', 'candy', 'salt', 'sugar']

# Testing list methods, see cars.py for description of methods used.

ingredients.append('soda')
print(ingredients)
ingredients.insert(0, 'pepper')
print(ingredients)
ingredients.remove('milk')
print(ingredients)
popped_ingredient = ingredients.pop(3)
print(f'{popped_ingredient.title()} has been removed from ingredients.')
print(ingredients)
del ingredients[0]
print(ingredients)
print(sorted(ingredients))
print(sorted(ingredients, reverse=True))
ingredients.sort()
print(ingredients)
ingredients.sort(reverse=True)
print(ingredients)
ingredients.reverse()
print(ingredients)
ingredients.reverse()
print(ingredients)
