import random

number = 0
userGuess = 0
lives = 6

name = input("Whats your name? ")

def generateNumber():
    global number
    number = random.randint(1, 100)

def guess():
    global userGuess
    userGuess = int(input("Hi " + name + ", please guess a number between 1 -100: "))

def userLives():
    global lives
    if lives > 1:
        lives = lives -1
        print (str(lives) + " Lives remaining")
    else:
        print ("You ran out of lives, the number I was thinking of was " + str(number))

def check():
    if userGuess == number:
        print ("Well done " + name + ", you guessed correctly!")
    elif userGuess > number:
        userLives()
        print (" Lower. guess again")
        guess()
        check()
    else:
        userLives()
        print ("Higher. Guess again")
        guess()
        check()

generateNumber()
guess()
check()
