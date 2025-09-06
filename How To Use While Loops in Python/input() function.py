message = input("What is your name? > ")
print(f'The name you gave us is: {type(message)}')

# ---------------------------------------------

age = int(input("What is your age> > "))

if age >= 18:
    print('You are allowed to drink')
else:
    print('Sorry only milk for you')

# ---------------------------------------------

age = input("What is your age> > ")

if age.isnumeric():
    age = int(age)
    if age >= 18:
        print('You are allowed to drink')
    else:
        print("Sorry only milk for you")
else:
    print('We need a number not a string')
    age = input("What is your age? > ")
    if age.isnumeric():
        age = int(age)
        if age >= 18:
            print('You are allowed to drink')
        else:
            print("Sorry only milk for you")







