# 45*3=555 , 56+9=77 ,56/6=4
num1=int(input("Enter the 1st number: "))
num2=int(input("Enter the 2nd number: "))
num3=input('so what you want ? * + /:')

if num1 ==45 and num2 ==3 and num3 =='*':
    print("555")
elif num1 ==56 and num2 ==9 and num3 =='+':
    print("77")
elif num1 ==56 and num2 ==77 and num3 =='/':
    print("4")
elif num3 =='+':
    plus=num1+num2
    print(plus)
elif num3 =='*':
    mul=num1*num2
    print(mul)
elif num3 =='/':
    div=num1/num2
    print(div)