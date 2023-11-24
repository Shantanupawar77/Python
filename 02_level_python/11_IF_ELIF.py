experience=int(input("Enter your experience:"))
grade=int(input("Enter your grede:"))

if (experience>10 and grade >90):
    print("Your salary is 1 Lakh.")
elif (experience>5 and experience<=10 ) and (grade >80 and grade <=90):
    print("Your salary is 80 Thounsands.")
elif (experience>3 and experience<=5 ) and (grade >70 and grade <=80):
    print("Your salary is 50 Thousands")
else:
    print("Give the proper input")
    

    