import time
print("Please insert Your CARD")
time.sleep(5)
password = 1234
pin = int(input("Enter your atm pin:"))
balance = 5000
if pin == password:
    while True:
        print(""" 
			1 == balance
			2 == withdraw balance
			3 == deposit balance
			4 == exit
			"""
              )

        try:    
             
            option = int(input("Please enter your choise "))
        except:
            print("Please enter valid option")
        
                
        if option == 1:
            print(f"Your current balance is {balance}")
                                     
        if option == 2:

            withdraw_amount = int(input("please enter withdraw_amount "))

            

            balance = balance - withdraw_amount

            print(f"{withdraw_amount} is debited from your account")

            

            print(f"your updated balance is {balance}")

            

        if option == 3:

            deposit_amount = int(input("please enter deposit_amount"))

            balance = balance + deposit_amount

            

            print(f"{deposit_amount} is credited to your account")



            print(f"your updated balance is {balance}")



        if option == 4:

            break


else:
    print("wrong pin Please try again")

