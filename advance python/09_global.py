a=45
def fubction1():
    global a
    print(f"print statement 1: {a}")
    a=9
    print(f"print statement 2:{a}")
fubction1()
print(f"print statement 3:{a}")