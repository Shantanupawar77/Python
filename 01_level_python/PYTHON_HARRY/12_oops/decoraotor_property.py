class Employeee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    @property
    def email(self):
        return f"{self.fname}.{self.lname}@codewithharry.com"
    @email.setter
    def email(self,string):
        print("setting now..")
        names=string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]
hindustani_supporter=Employeee("Hindustani","Supporter")
print(hindustani_supporter.email)
hindustani_supporter.fname="US"
print(hindustani_supporter.email)
hindustani_supporter.email="this.that@codewithharry.com"
print(hindustani_supporter.email)
