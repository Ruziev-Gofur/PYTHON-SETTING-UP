# list of integers
number_list = [1, 2, 3, 4, 5]

# list of strings
strings_list = ["Frodo", "Samwise", 'Gandalf', 'Aragorn']

# a mixed list (int, string, float, bool)
mixed_list = [42, "Hello", 3.14, False]

print(number_list)
print(strings_list)
print(mixed_list)

print(number_list[0])
print(strings_list[2])
print(mixed_list[-2])

print(f"There is only {number_list[0]} "
      f"{strings_list[2].upper()} in the room")