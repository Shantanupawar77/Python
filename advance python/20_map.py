def square(num):
    return num*num
l1=[1,2,3,4]
#method 1
l2=[]
for item in l1:
    l2.append(square(item))
print(l2)

#method 2
print(list(map(square,l1)))
