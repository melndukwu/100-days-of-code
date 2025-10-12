import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
number = random.randint(1, 100)

def game(difficulty):
    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5

    for c in range(attempts, 0, -1):
        print(f"You have {c} remaining to guess the number.")
        user_guess = int(input("Make a guess: "))

        if user_guess == number:
            print(f"You got it! The answer was {number}.")
            return

        elif user_guess > number:
            print("Too high.")
        else:
            print("Too low.")

        if c - 1 == 0:
            print("You've run out of guesses, you lose.")
            print(f"The number was {number}.")

game(user_choice)