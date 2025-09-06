available_items = [
    "bananas", "bread", "milk", "tomatoes", "lettuce",
    "pineapple", "chicken", "rice", "pasta", "cucumbers",
    "yogurt", "chocolate"
]

groceries = [
    "apples", "bananas", "bread", "milk", "tomatoes",
    "egge", "flour", "cheese"
]

for item in groceries:
    if item not in available_items:
        print(f"{item} not available")


# favorite_fruits = ['apple', 'banana', 'cherry']
# fav_fruit = 'apple'
#
# for fruit in favorite_fruits:
#     if fruit == fav_fruit:
#         print(f'{fruit} is the best')
#     else:
#         print(fruit)

# if fruit not in favorite_fruits:
#     print(f'This is a disgrace {fruit} is amazing!')
# else:
#     print('Good fruits list')




