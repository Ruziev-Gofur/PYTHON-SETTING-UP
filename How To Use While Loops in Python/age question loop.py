age = input("What is your age> > ")

while not age.isnumeric():
    age = input("What is your age> > ")

    if age.lower() == 'stop':
        break
else:
    age = int(age)
    if age >= 18:
        print('You are allowed to drink')
    else:
            print("Sorry only milk for you")
