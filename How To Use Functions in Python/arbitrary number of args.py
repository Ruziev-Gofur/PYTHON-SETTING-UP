# def sum_numbers(*args):
#     print(type(args))
#     total = 0
#     for number in args:
#         total += number
#     return total
#
# result = sum_numbers(10, 20, 30, 40, 50)
# print(f"The sum is: {result}")

def create_user_profile(username, email, **kwargs):
    profile = {
        'username': username,
        'email': email,
    }

    for atribute, value in kwargs.items():
        profile[atribute] = value

    return profile

user_profile = create_user_profile(
    "Jorj", "Jorj@gmail.com",
    age = 18, location = 'America',
    interestes = ['Cycling', 'Hiking']
)
print(user_profile)