class Vehicles:
    def __init__(self,name,wheels,seats):
        self.name=name
        self.wheels=wheels
        self.seats=seats

tata=Vehicles("TATA NANO",4,4)
TVS=Vehicles("JUPITER",2,2)
royal_enfield=Vehicles("BULLET",2,5)

print("The name of the vehicle is {} ,it is having {} wheels and it can carry max of {} peoples".format(royal_enfield.name,royal_enfield.wheels,royal_enfield.seats))
