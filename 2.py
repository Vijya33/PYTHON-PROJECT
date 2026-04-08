import random

# Generate random number between 1 and 100
number = random.randint(1, 100)

attempts = 0
guess = None

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100")

# Loop until the user guesses correctly
while guess != number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess > number:
        print("Too high! Try again.")

    elif guess < number:
        print("Too low! Try again.")

    else:
        print("Correct! You guessed the number.")
        print("Total attempts:", attempts)