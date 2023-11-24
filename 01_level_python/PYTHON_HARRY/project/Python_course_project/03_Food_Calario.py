print("Enter the number of elements in list one by one:\n")
size=int(input("Enter the size of the list\n"))
myList=[]
for i in range(size):
    myList.append(int(input("Enter the elemenet\n")))

reverse1=myList[:]
reverse1.reverse()
print(f"My first reversed list of {myList} is {reverse1}")


reverse2=myList[::-1]
print(f"My second reversed list of {myList} is {reverse2}")

reverse3=myList[:]
for i in range((len(reverse3))//2):
    reverse3[i],reverse3[(len(reverse3))-i-1]=reverse3[(len(reverse3))-i-1],reverse3[i]
print(f"My third reversed list of {myList} is {reverse2}")

if(reverse1==reverse2)and (reverse3==reverse2):
    print("All the reversed lists are same .")