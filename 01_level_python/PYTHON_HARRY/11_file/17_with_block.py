#f=open("shantanu.txt","rt")
#f.close()
with open("shantanu.txt","rt") as f:
    a=f.read(4)
    print(a)