with open('sample_write.txt','r') as f:
    a=f.read()
print(a)
#no need to close the file
with open('sample_write.txt','w') as f:
    a=f.write()
print(a)