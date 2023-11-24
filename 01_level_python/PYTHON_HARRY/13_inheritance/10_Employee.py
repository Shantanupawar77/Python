class Employee:
    salary=1000
    increment=1.5

    @property
    def salaryAfterIncreament(self):
        return self.salary*self.increment

    @salaryAfterIncreament.setter
    def salaryAfterIncrement(self,sai):
        self.increment=sai/self.salary

e=Employee()
print(e.salaryAfterIncrement)
print(e.increment)
e.salaryAfterIncrement=4000
print(e.salaryAfterIncrement)
print(e.increment)


