class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
        
    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train is {self.seats}")

    def getInfo(self):
        print(f"The price of the ticket is :Rs {self.fare}")
    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked !your seat number is {self.seats}")  
            self.seats=self.seats-1
        else:
            print("Sorry this train is full kindly try in tatkal")  
Marathwada = Train("Marathwada",30,4)
Marathwada.getInfo()
Marathwada.bookTicket()
Marathwada.getStatus()


