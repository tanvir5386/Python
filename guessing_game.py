import random

secret = random.randint(1, 100)
guess = 0

while guess != secret:
    guess = int(input("Guess the number (1-100): "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")

print("Congratulations! You guessed it!")