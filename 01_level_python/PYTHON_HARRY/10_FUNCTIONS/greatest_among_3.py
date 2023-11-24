def greatest(num1,num2,num3):
   # num1=int(input('Enter the num1:'))
   # num2=int(input('Enter the num2:'))
    #num3=int(input('Enter the num3:'))

    if num1>num2:
        if num1>num3:
            print(f"{num1} is greatest")
        else:
            print(f"{num3} is greatest")

    else:
        if num2>num3:
            print(f"{num2} is greatest")
        else:
            print(f"{num3} is greatest")
        
greatest()