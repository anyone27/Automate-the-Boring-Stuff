import random

name = input("Hello, what is your name? ")

print ("Well, " + name + ", I am thinking of a number between 1 and 100, can you guess it in 6 turns?")
secretNumber = random.randint (1, 100)

for guessesTaken in range (1, 7):
    print ("Take a guess.")
    guess = int(input())

    if guess < secretNumber:
        print ("Your guess is too low.")
    elif guess > secretNumber:
        print ("Your guess is too high.")
    else:
        break

if guess == secretNumber:
    print ("Good job, " + name + "! You guessed the number in " + str(guessesTaken) + " guesses!")
else:
    print ("Bad luck " + name + ". The number was " + str(secretNumber) + ".")
    
