b=set()
b.add(3)
b.add(4)
b.add(5)
b.add(6)
b.add(3)
b.add(8)
b.add(5)
#b.add([23,67,89])#--->cannot use
b.add((23,67,89))#--->can use
#b.add({23:54})#--->cannot use
print(b)
print(len(b))
b.remove(8)
print(b)
print(b.pop())
print(b)