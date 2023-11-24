l=10

def function1():
    #l=5
    m=8
    global l
    l=l+55 #--->it throws an error without giving global keyword 
    print(l,m)
function1() 