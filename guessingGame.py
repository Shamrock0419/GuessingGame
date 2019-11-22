import random
value = random.randint(1,101)
guess = int(input("I am thinking of a number between one through one hundred. Enter your guess: "))
if guess > value:
    print("guess is too high")
elif guess < value:
    print("value is too low")
else :
    print("You got it!")