me="shantanu"
rNo="nine"
#1
w="This is %s and has roll number %s "%(me,rNo)
print(w)
#2
w="This is {} and has roll number {} "
b=w.format(me,rNo)
print(b)
#3
r=f"This is {me} and has roll number {rNo}"
print(r)