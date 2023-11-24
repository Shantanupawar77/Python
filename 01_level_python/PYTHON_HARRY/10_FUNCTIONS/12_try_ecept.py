num1=input("Enter the num1:\n")
num2=input("Enter the num2:\n")
try:
    print("The sum of these two numbers is",int(num1)+int(num2))
except Exception as e:
    print(e)
print("This is very important")