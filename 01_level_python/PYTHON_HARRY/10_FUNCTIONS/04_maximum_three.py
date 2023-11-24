n1=int(input("ENTER THE N1:\n"))
n2=int(input("ENTER THE N2:\n"))
n3=int(input("ENTER THE N3:\n"))

def max(num1,num2,num3):
    if num1>num2:
        if num1>num3:
            return num1
        else:
            return num3
    else:
        if num2>num3:
            return num2
        else:
            return num3

m=max(n1,n2,n3)
print("The maximum among the three numbers is "+str(m)+".")