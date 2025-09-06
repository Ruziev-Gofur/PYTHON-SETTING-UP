from itertools import count

groceries = [
    "milk", "cheese", "eggs", "chicken", "bread", "apples",
    "bananas", "chicken", "rice", "carrots", "yogurt", "chicken",
    "yogurt", "chicken", "apples", "bananas", "chicken",
]

count = 0
print(f"List length: {len(groceries)}")
print(groceries)

for item in groceries:
    count += 1
    if item == "chicken":
        groceries.remove(item)

# while 'chicken' in groceries:
#     groceries.remove('chicken')
#     count += 1

print(groceries)
print(f"Count is: {count}")