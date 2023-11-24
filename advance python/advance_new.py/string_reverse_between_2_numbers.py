t=input()
a=t[ :t.find('h')+1]
b=t[t.find('h'):]
c=t[t.find('h')+1 :t.rfind('h')]

if t.count('h')>=2:
    print(a+ c[ : :-1]+b)