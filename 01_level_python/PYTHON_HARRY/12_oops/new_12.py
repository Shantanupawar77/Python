class Employee:
    no_of_leaves=7
    def printdetails(self):
        return f"Name is {self.name} ,role is {self.role} , std is {self.std}"
harry=Employee()
rohan=Employee()

harry.name="Harry"
harry.salary=345667
harry.role="Instructor"

rohan.name="Rohan"
rohan.std= 11
rohan.role="Stduent"

print(rohan.printdetails())