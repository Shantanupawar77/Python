a = 0
b = 1
n=int(input())    
if n < 0:
    print("Incorrect input")
elif n == 0:
    print(0)
elif n == 1:
    print(b)
else:
    for i in range(1, n):
        c = a + b
        a = b
        b = c
    print(b)