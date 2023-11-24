# a=input()
# print(a.replace("1","one"))
# print(a.replace("@"," "))
# s=input()
# a=s[s.find("h")+1:s.rfind("h")]
# print((s[:s.find("h")+1])+a.replace("h","H")+ s[s.rfind("h"): ])
s=input()
n=""
for i in range(len(s)):
    if i%3 !=0:
        n+=s[i]
print(n)