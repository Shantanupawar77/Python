class Employee:
    company="Google"
    salary=100
    age=8
harry=Employee()
rajni=Employee()
harry.salary=1234
harry.age=90
print(rajni.salary)
print(harry.salary)
print(rajni.company)
print(harry.company)
print(harry.age)