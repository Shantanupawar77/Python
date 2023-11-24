class Employee:
    salary=100

    @classmethod
    def changeSalary(cls,sal):
        cls.salary=sal

e=Employee()
print(e.salary)
e.changeSalary(888)
print(e.salary)

