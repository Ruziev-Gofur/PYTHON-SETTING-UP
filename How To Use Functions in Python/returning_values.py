from django.db.models.expressions import result


def calculyator(x, y, z):
    result = x + y + z
    return result

# value = calculyator(5,12,8)
# print(f"Result of calculyator function is {value}")

while True:
    print("Enter teh values your want to add")
    num1 = int(input("Number1: "))
    num2 = int(input("Number2: "))
    num3 = int(input("Number3: "))

    print("Result of calculyator function: "
          f"{calculyator(num1, num2, num3)}")
