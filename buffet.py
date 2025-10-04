buffet_items = ('macaroni', 'pizza', 'salad', 'roast beef', 'crab') #original buffet items
for item in buffet_items:
    print(item)

try:
    buffet_items[0] = 'macaroni n cheese' #We try to change an individual value within the tuple are are met with an error
except:
    TypeError
    print('This causes an error, we cannot change a tuple')

buffet_items = ('macaroni', 'pizza', 'salad', 'eggs', 'bacon') #we change the values of the tuple by overwriting the variable
for item in buffet_items:
    print(item)


