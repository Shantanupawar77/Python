from functools import reduce

l=[12,34,33,21,34,25,678,986,389965,2467,3,673,45,38]
a=reduce(max,l)
print(a)