import random

guessesTaken = 0

value = random.randint(1,101)
while guessesTaken < 10:
    guess = int(input("I am thinking of a number between one through one hundred. Enter your guess: "))
    
    guessesTaken = guessesTaken + 1

    if guess > value:
        print("guess is too high, try again")

    elif guess < value:
        print("guess is too low, try again")

    else :
        print("You got it! You guessed the number in " + str(guessesTaken) + " attempts!")
        break 

if guessesTaken == 10:
    print("Sorry, the number I was thinking of was " + str(value))

