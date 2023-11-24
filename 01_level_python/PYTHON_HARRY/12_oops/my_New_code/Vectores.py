class C2dVec:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j
    def __str__(self):
        return f"{self.icap}i+{self.jcap}j"
        
class C3dVec(C2dVec):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap=k
    def __str__(self):
        return f"{self.icap}i+{self.jcap}j+{self.kcap}k"
v2=C2dVec(1,7)
v3=C3dVec(4,8,7)
print(v2)
print(v3)
        