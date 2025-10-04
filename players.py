players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:6:2])
# List slices take a selection from an existing list
#First number is where slice will start, second where it will stop, 3rd number is the interval, all seperated by ":"

print(players[-2:]) #use a negative number for the first number to get the items from the end of the list

print('Here are the first four players of my team:')
for player in players[:4]: # here we can use the slice in a "for" loop
    print(player.title())

print('Here are the middle 3 players of my team: ')
print(players[1:4])

print('Here are the last three players of my team: ')
print(players[-3:])
