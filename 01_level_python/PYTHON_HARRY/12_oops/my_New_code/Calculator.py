class Calculator:
    pass
    def __init__(self,num):
        self.number=num
    @staticmethod
    def greet():
        print("Hello ,thanks for using me !")
    def square(self):
        print(f"The square of {self.number} is {self.number **2}")
    def squareroot(self):
        print(f"The squareroot of {self.number} is {self.number **0.5}")
    def cube(self):
        print(f"The cube of {self.number} is {self.number **3}")
    
    
num1=Calculator(9)
num1.greet()
num1.square()
num1.squareroot()
num1.cube()
