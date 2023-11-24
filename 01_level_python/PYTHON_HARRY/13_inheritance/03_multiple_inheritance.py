class Employee:
    company ="visa"
    eCode=120

class Freelancer:
    company="Fivver"
    level=0

    def upgradelevel(self):
        self.level=self.level+1

class Programmer(Employee,Freelancer):
    name="ROHIT"

P=Programmer()
P.upgradelevel()
print(P.level)
print(P.company)