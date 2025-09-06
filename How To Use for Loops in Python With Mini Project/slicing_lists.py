pizza_toppings = [
    'Pepperoni',
    'Mushrooms',
    'Onions',
    'Sausage',
    'Pepperoni222',
    'Mushrooms222',
    'Onions222',
    'Sausage222',
]

print('The first 5 toppings only:')
print(pizza_toppings[2:5])

print()

print(pizza_toppings[:4])
print(pizza_toppings[6:])

print()

for topping in pizza_toppings[2:6]:
    print(f"I only like {topping} on my Pizza")


