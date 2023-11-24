n=18
number_guesses=1
print("Number of guesses is limited to only 9 times :")
while number_guesses<=9:
    guess_number=int(input("Guess the number :\n"))
    if guess_number<18:
        print("you enter less number please enter the greater number.\n")
    elif guess_number>18:
        print("you enter greater number please enter the smaller number.\n")
    else:
        print("You win\n")
        print(number_guesses,"No.of guesses to finish")
        break
    print(9-number_guesses,"no. of guesses left ")
    number_guesses=number_guesses+1
if(number_guesses>9):
    print("Game over")
