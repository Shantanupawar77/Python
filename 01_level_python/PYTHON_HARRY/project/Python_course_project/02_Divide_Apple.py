# n=int(input("Enter the Number of apples:\n"))
# mn=int(input("Enter the minimum value of student:\n"))
# mx=int(input("Enter the maximum value of student:\n"))
# for i in range(mn,mx+1):
#     if(mn==mx):
#         print("This is not a range.")
#     if(n%i==0):
#         print(f"{i} is divisor of {n}")
#     else:
#         print(f"{i} is not a divisor of {n}")
try:
    n=int(input('Enter the value for the n :'))
    mx=int(input('Enter the value for the mx :'))
    mn=int(input('Enter the value for the mn :'))

except ValueError:
    print('Enter integers only ')
    exit()

if mn>=mx:
    print('This can not be the range as the min should be less than max')
if(mn==mx):
    print("This is not a range.")

for i in range (mn,mx+1):
    if n%i==0:
        print(i,'is a divisor of',n)
    else:
        print(i,'is not a divisor of',n)
