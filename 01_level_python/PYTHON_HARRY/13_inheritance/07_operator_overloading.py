class Number:
    def __init__(self,num):
        self.num=num

    def __add__(self,num2):
        print("Lets add")
        return self.num+num2.num

    def __mul__(self,num2):
        print("Lets multiply")
        return self.num*num2.num
    def __sub__(self,num2):
        print("Lets substract")
        return self.num-num2.num
    def __str__(self):
        return f"Decimal number :{self.num}"
    
n1=Number(10)
print(n1)
##sum=n1+n2
#mul=n1*n2
#sub=n1-n2
##print(mul)
#print(sub)