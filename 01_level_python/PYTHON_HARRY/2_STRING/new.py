#s=input()
#c=s.count("f")
#print(s.find('f',s.find('f')+1))

#a=input()
#print(a.replace('1','one'))
s=input()
n=""

for i in range(len(s)):
    if i % 3 !=0:
        n +=s[i]
    
print(n)
