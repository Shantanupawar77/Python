print(ord('r'))
print(oct(23))
print(hex(23))
print(bin(10900))
a=chr(72)
print(a)

str1="SHANTANU"
st1_count=str1.count('A',0,3)
print(st1_count)
str1_find=str1.find('A',0)
print(str1_find)
str1_index=str1.index('A')
print(str1_index)
# Python find() produces -1 as output if it is unable to find the substring, whereas index() throws a ValueError exception.