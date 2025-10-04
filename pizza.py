pizzas = ['pepperoni', 'onion', 'sausage', 'pineapple', 'jalapeno']

for pizza in pizzas:
    print(f'I really like {pizza} pizza.')
print('I love pizza')

friends_pizzas = pizzas[:]

pizzas.append('cheese')
friends_pizzas.append('ham')

print('My favorite pizzas are:')
print(pizzas)

print('\nMy friends favorite pizzas are:')
print(friends_pizzas)