num=int(input("Enter the number:\n"))
prime=True
for i in range(2,num):
    if(num%i==0):
        prime=False
        break
if prime:
    print("Given number is prime.")
else:
    print("Given number is not prime.")