class Calculator:
    def __init__(self,num):
        self.num=num
    def square(self):
        print(f"The value of {self.num} square is {self.num ** 2}")
    def squareRoot(self):
        print(f"The value of {self.num} square is {self.num ** 0.5}")
    def cube(self):
        print(f"The value of {self.num} square is {self.num ** 3}")

    @staticmethod
    def greet():
        print("Hello there welcoome to the best calculater")
    @staticmethod
    def ty():
        print("Thank you for using the calculator")

a=Calculator(4)
a.greet()     
a.square()
a.squareRoot()
a.cube()
a.ty()