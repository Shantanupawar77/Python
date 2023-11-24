print("How Many Row You Want To Print")
num1= int(input())
print("Type 1 Or 0")
num2 = int(input())
new =bool(num2)
if new == True:
    for i in range(1,num1+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif new ==False:
    for i in range(num1,0,-1):
        for j in range(1,i+1):
            print("*", end="")
        print()