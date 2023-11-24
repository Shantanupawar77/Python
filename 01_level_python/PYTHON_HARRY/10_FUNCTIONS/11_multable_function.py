def multable(n):
    for i in range(1,11):
        print(f"{n}*{i}={n*i}") 
num=int(input("ENTER THE VALUE FOR NUM which you want to have multable:\n"))
multable(num)