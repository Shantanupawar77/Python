class Programmer:
    company="Microsoft"
    def __init__(self,name,salary,id):
        self.name=name
        self.salary=salary
        self.id=id
    def printDetails(self):
        print(f"The name of the programmer is {self.name}")
        print(f"The company of the programmer is {self.company}")
        print(f"The salary of the programmer is {self.salary}")
        print(f"The id of the programmer is {self.id}")

shantanu=Programmer("Shantanu","80k","777")
savta=Programmer("Savta","99k","455")
#shantanu.printDetails()
savta.printDetails()

