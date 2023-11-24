def next_palimdrome_(n):
    n=n+1
    while not is_palimdrome_(n):
        n+=1
    return n
def is_palimdrome_(n):
    return str(n)==str(n)[::-1]

if __name__=="__main__":
    size=int(input("Enter the size of list :\n"))
    num_list=[]
    for i in range(size):
        num_list.append(int(input("Enter the element:")))
    print(f"Your entered list is {num_list}.")
    new_list=[]
    for element in num_list:
        if(element>10):
            n=next_palimdrome_(element)
            new_list.append(n)
        else:
            new_list.append(element)
    print(f"Your list is{new_list}.")