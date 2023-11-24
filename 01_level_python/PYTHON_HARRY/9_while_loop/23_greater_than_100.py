while(True):
    inp=int(input("Enter the number:\n"))
    if inp>100:
        print("Congrats you have entered a number greater than 100")
        break
    else:
        print("Try again")
        continue