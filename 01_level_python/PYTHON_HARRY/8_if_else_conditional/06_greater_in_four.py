num1=int(input("Enter the num1 : "))
num2=int(input("Enter the num2 : "))
num3=int(input("Enter the num3 : "))
num4=int(input("Enter the num4 : "))
if(num1>num2):
    f1=num1
else:
    f1=num2

if(num3>num4):
    f2=num3
else:
    f2=num4
if(f1>f2):
    print(str(f1)+" is greatest")
else:
    print(str(f2)+" is greatest")