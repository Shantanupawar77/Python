#iterative
'''def factorial(n):
    fac =1
    for i in range(n):
        fac = fac *(i+1) 
    return fac
number=int(input("Enter the number:"))
print(factorial(number))'''
#recursive
def factorial(n):
    
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
number=int(input("Enter the number:"))
print(factorial(number))