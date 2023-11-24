class Employee:
    no_of_leaves=34
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def __add__(self,other):
        return self.salary+other.salary
    def __truediv__(self,other):
        return self.salary/other.salary
    def __repr__(self):
        return f"Employee('{self.name}',{self.salary},'{self.role}')"
    def __str__(self):
        return f"Employee(The name is {self.name},salary {self.salary},role is{self.role})"

emp1=Employee("Harry",4500,"Coordinator")
#emp2=Employee("Rohan",45,"cleaner")
print(str(emp1))