def increment(num):
    try:
        return int(num)+1
    except:
        raise ValueError("This is not good ")
a=increment("dfgt56")
print(a)