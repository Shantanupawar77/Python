def next_palimdrome_(n):
    n=n+1
    while not is_palimdrome_(n):
        n+=1
    return n
def is_palimdrome_(n):
    return str(n)==str(n)[::-1]



if __name__=="__main__":
    n=int(input("Enter the how many test cases you want:\n"))
    numbers_=[]
    for i in range(n):
        number_=int(input("Enter the number"))
        numbers_.append(number_)
    for i in range(n):
        print(f"Next palimdrome for {numbers_[i]} is {next_palimdrome_(number_[i])}")