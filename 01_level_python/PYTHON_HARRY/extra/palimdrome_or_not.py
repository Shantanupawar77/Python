str1=input("Enter a string:\n")
str2=str1[::-1]
print(str2)
isPalimdrome=False
for i in range(int(len(str1)/2)):
    if(str1[i]==str2[i]):
        isPalimdrome=True
if(isPalimdrome):
    print("Given string is palimdrome")
else:
    print("Given string is not  palimdrome")