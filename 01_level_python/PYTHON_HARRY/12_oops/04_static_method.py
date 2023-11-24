class Employee:
    company="Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")
    @staticmethod
    def greet():
        print("Good morning ,sir")
    @staticmethod
    def time():
        print("9:00")
harry=Employee()
harry.salary=100000
harry.company="MICROSOFT"
harry.getSalary()  #Employee.getSalary(harry)
harry.greet()
harry.time()
