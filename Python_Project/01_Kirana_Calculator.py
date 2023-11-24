               # Kirana Store #
sum=0
while(True):
    userInput=input("Enter the item price or press 'q' to quit:\n")
    if(userInput!='q'):
        sum=sum+int(userInput)
        print(f"Your bill so far {sum}:")

    else:
        print("Thanks for shopping with us")
        print(f"Your total bill is {sum}.")
        break