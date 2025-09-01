car_brands = [
    "Total",
    "Ford",
    "Honda",
    "Chevrolet",
    "Tesla",
    "BMW"
]
print(car_brands)

print('After modifying Ford to Audi')
car_brands[1] = 'Audi'
print(car_brands)

print('After adding Mercedes-Benz')
# car_brands.append('Mercedes-Benz')
car_brands.insert(0, 'Mercedes-Benz')
print(car_brands)

print('After removing Honda')
del car_brands[3]
print(car_brands)



