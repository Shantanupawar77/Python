
def count_c_v():
    conew=0
    vonew=0
    for st in str1:
        if(st=='a'or st=='e'or st=='i'or st=='o'or st=='u'or st=='A'or st=='E'or st=='I'or st=='O'or st=='U'):

            vonew=vonew+1
        else:
            conew=conew+1
    print("The number of vowels in given word "+str(vonew))
    print("The number of consonants in given word "+str(conew))
str1=input("Enter the word:\n")

count_c_v()





