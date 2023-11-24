def greater_than_five(num):
    if num>5:
        return True
    else:
        return False
l=[1,2,3,4,5,6,7,8,45,6,72,1,2,34,4,5]
print(list(filter(greater_than_five,l)))