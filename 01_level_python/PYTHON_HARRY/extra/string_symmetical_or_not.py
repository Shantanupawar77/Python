str1="khokho7"
half=int(len(str1)/2)
if len(str1)%2==0:
    first_str1=str1[:half]
    second_str1=str1[half:]
else:
    first_str1=str1[:half]
    second_str1=str1[half+1:]

if first_str1==second_str1:
    print(str1,"String is symmetrical")
else:
    print(str1,"String is not  symmetrical")