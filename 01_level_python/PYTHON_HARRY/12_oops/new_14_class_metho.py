class Employee:
    best=90
    @classmethod
    def Upadate_score(cls,New_best):
        cls.best=New_best



shantanu=Employee()
shantanu.Upadate_score(99)
print(shantanu.best)
