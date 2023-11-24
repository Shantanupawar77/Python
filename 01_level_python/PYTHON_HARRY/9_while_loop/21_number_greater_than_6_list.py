items=[int,float,"harry","shantanu",89,9,2,34,5,7,6,1,12]

for item  in items:
    if str(item).isnumeric() and item>6:
        print(item)