class A:
    def met(self):
        print("This ia a class A")
class B(A):
    def met(self):
        print("This ia a class B")
class C(A):
    def met(self):
        print("This ia a class C")
class D(C,B):
    pass
a=A()
b=B()
c=C()
d=D()
d.met()