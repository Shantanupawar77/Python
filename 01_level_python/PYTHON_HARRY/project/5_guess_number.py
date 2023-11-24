import random
randNO=random.randint(1,100)

nGuess=int(input("Guess the number:\n"))

if randNO < nGuess :
    print("Lesser number please!")
elif randNO > nGuess :
    print("Greater number please!")
else:
    print("You guessed it right!")

