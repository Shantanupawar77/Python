# l = [1, 2, 3, 4, 5, 6, 78, 9, 0, 90, 89, 0,
#      90, 80, 45, 35, 245, 67, 80623, 55, 55, 85]
# a = filter(lambda a: a % 5 == 0, l)
# print(list(a))

a=int(input())
b=int(input())
c=int(input())
d=int(input())
i=0
while 1:
    i=i+1
 
    if(c==a+i) and (d==b+i):
        print('YES')
        
        break
    elif (c==a-i) and (d==b-i):
        print('YES')
        
        break
    elif ((c==a-i) and (d==b+i)) or ((c==a+i) and (d==b-i)):
        print('YES')
        break
    elif(i==7):
          print('NO')
          break



 