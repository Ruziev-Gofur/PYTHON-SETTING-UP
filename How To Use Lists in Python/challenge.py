# Step 1: Create a list of name
print('Original List')
guests = [
    'Frodo',
    'Sam',
    'Gandalf',
    "Legolas",
    "Aragorn"
]
print(guests)

# Step 2: Print out a personalized message to 3 of them
print('Personalized Invitations: ')
print(f'Hi {guests[0]} hope your have the ring with you.')
print(f'{guests[3]} don\'t forget to leave your bow at the door.')
print(f'{guests[2]} no funny magic business. Understood')

# Step 3: Adding 3 new guests in different positions
guests.append('Bilbo')
guests.insert(3, 'Saruman')
guests.insert(len(guests)//2, 'Saruman111')
guests.remove('Saruman')
guests.insert(0, 'Galadriel')
print(guests)
print()

# Step 4: print the length of the list
print('Length of the list is now: ',len(guests))
print()

import random

# Step 5 Remove 1 random person and 1 specific person
print('Removing Aragorn:')
guests.remove('Aragorn')
print(guests)
print('Removing 1 random person')
# del guests[5]
del guests[random.randint(0, len(guests))]
print(guests)

# Step 6 Organize the party
sorted_guests = sorted(guests)
print('Sorted list of guests:', sorted_guests)
print('Orginal List: ', guests  )







