# Step #1: Get the name of the stadium
# stadium_name = input("Enter the name of the stadium: ")
#
# # Step #2: Print out the name of the stadium in ALL CAPS
# print(stadium_name.upper())
#
# # Step #3: Get inputs for the width and the length of the field
# width = float(input('Enter the width of the field in KM: '))
# length = float(input('Enter the length of the field in KM: '))
#
# # Step #4 print out the area of the field
# area = width * length
# print(f'The area of the {stadium_name} is {area} square KM')

# Step #5 Calculate the cose per seat without Discount
totalSeats = 152905
totalCost = 1_000_000
costPerSeat = totalCost / totalSeats
print(f'The cost per seat is: {costPerSeat: .2f}')

# Step #6 Calculate the cost per seat with a 60% discount
discount = 0.6
discountCostPerSeat = costPerSeat * (1 - discount)
totalSavings = totalCost - (discountCostPerSeat * totalSeats)

# print out a full accounting
print(f"Cost per seat with 60% discount: ${discountCostPerSeat: .2f}")
print(f"Total savings: ${totalSavings: .2f}")













