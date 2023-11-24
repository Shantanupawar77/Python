class Employee:
    company="Google"
    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("Its very amazing")
    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")


    @staticmethod
    def greet():
        print("Good morning ,sir")
    @staticmethod
    def time():
        print("9:00")
harry=Employee("HARRY",10000,"youtube")
harry.getDetails()