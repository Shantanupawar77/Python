percentage=int(input("Enter your percentage:\n"))
if percentage>=90:
    print("Grade is A+")
elif percentage<90 and percentage>=80:
    print("Grade is A")
elif percentage<80 and percentage>=70:
    print("Grade is B")
elif percentage<70 and percentage>=60:
    print("Grade is C")
elif percentage<60 and percentage>=50:
    print("Grade is D")
elif  percentage<50 and percentage>=40:
    print("Grade is E")
else:
    print("Your grade is F")