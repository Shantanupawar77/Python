class Person:
    country="India"

    def takeBreath(self):
        print("I am breathing")
class Employee(Person):
    company="Honda"
      
    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print(f"I am an Employee so I am luckily breathing..")

class Programming(Employee):
    company="Fiver"

    def getSalary(self):
        print("No salary to programmers !")
    def takeBreath(self):
        print(f"I am an programmer so I am ++++luckily breathing..")


p=Person()
p.takeBreath()
e=Employee()
pr=Programming()
pr.takeBreath()
print(pr.country)