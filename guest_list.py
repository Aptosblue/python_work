guest_list = ['elliott', 'brian', 'kristen', 'hope', 'reece', 'luke']

print(f'{guest_list[0].title()}, you have been invited to dinner tomorrow night.')
print(f'{guest_list[1].title()}, you have been invited to dinner tomorrow night.')
print(f'{guest_list[2].title()}, you have been invited to dinner tomorrow night.')
print(f'{guest_list[3].title()}, you have been invited to dinner tomorrow night.')
print(f'{guest_list[4].title()}, you have been invited to dinner tomorrow night.')
print(f'{guest_list[5].title()}, you have been invited to dinner tomorrow night.')

removed_guest = guest_list.pop(0)
print(f'{removed_guest.title()} cannot make it.')
guest_list.insert(0, 'bryton')

print(f'{guest_list[0].title()}, you have been invited to dinner tomorrow night.')
print(f'{guest_list[1].title()}, you have been invited to dinner tomorrow night.')
print(f'{guest_list[2].title()}, you have been invited to dinner tomorrow night.')
print(f'{guest_list[3].title()}, you have been invited to dinner tomorrow night.')
print(f'{guest_list[4].title()}, you have been invited to dinner tomorrow night.')
print(f'{guest_list[5].title()}, you have been invited to dinner tomorrow night.')

print('We found a bigger table.')
guest_list.insert(0, 'gaby')
guest_list.insert(3, 'beth')
guest_list.append('peyton')


for guest in guest_list:
    print(f'{guest.title()}, you have been invited to dinner tomorrow night.')

print('Actually, I lied, in fact, I only have room for 2 people')

popped_guest = guest_list.pop()
print(f"{popped_guest.title()}, sorry but you're uninvited.")

popped_guest = guest_list.pop()
print(f"{popped_guest.title()}, sorry but you're uninvited.")

popped_guest = guest_list.pop()
print(f"{popped_guest.title()}, sorry but you're uninvited.")

popped_guest = guest_list.pop()
print(f"{popped_guest.title()}, sorry but you're uninvited.")

popped_guest = guest_list.pop()
print(f"{popped_guest.title()}, sorry but you're uninvited.")

popped_guest = guest_list.pop()
print(f"{popped_guest.title()}, sorry but you're uninvited.")

popped_guest = guest_list.pop()
print(f"{popped_guest.title()}, sorry but you're uninvited.")

for guest in guest_list:
    print(f'{guest.title()}, congratulations you made the cut to be invited to my irrelevant dinner')

print(f'We are inviting {len(guest_list)} guests to dinner.')


