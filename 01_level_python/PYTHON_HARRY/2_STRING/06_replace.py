letter='''Dear  NAME ,
     *******************
       YOU ARE SELECTED
     *******************
       Date:  DATE '''
name=input("Enter the name\n")
date=input("Enter Date\n")
letter=letter.replace("NAME",name)
letter=letter.replace("DATE",date)
print(letter)