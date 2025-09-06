import random

number_to_guess = random.randint(1, 100)
guess = None
attempts = 0

while guess !=number_to_guess:
    guess_import = input('Guess a number between 1 and 100: ')

    if guess_import.isdigit():
        guess = int(guess_import)
        attempts += 1

        if guess < number_to_guess:
            print("Too low")
        elif guess > number_to_guess:
            print("Too high")
    else:
        print("Please enter a integer")

print(f"Coungratulation! your guessed the right num: {number_to_guess}")
print(f"It only took you {attempts} attempts")