z=int(input("Enter the value for n:\n"))
def sum(n):
    if n==0:
        return 0
    else:
        p=n=n+sum(n-1)
        return p
s=sum(z)
print("The sum of n natural numbers is ",s)