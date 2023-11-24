class Employee:
    no_of_leaves=7
harry=Employee()
rohan=Employee()

harry.name="Harry"
harry.salary=345667
harry.role="Instructor"

rohan.name="Rohan"
rohan.std= 11
rohan.role="Stduent"
print(Employee.no_of_leaves)
Employee.no_of_leaves= 11 #but rohan.no_of_leaves cannot work.
print(Employee.no_of_leaves)
