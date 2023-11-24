import random
def RohansMultiplication(number):
    wrong=random.randint(0,9)
    table=[number*i for i in range(1,11)]
    table[wrong]=table[wrong]+random.randint(0,10)
    return table
def isCorrect(table,number):
    for i in range(1,11):
        if table[i-1]!=i*number:
            return i-1
    return None
if __name__=="__main__":
    n=int(input("Enter the number which want multable:\n"))
    myTable=RohansMultiplication(n)
    print(myTable)
    indexError=isCorrect(myTable,n)
    print(f"The table is wrong at index {indexError}.")