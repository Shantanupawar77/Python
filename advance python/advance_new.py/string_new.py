t=input()
a=t.find('h')
b=t.rfind('h')
if t.count('h')>=2:
    print(t[ :a] + t[b+1 :])