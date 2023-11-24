from unicodedata import name


class Train:
    pass
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    def getStatus(self):
        print(f"The name of the Train is {self.name}")
        print(f"The fare of the Train is {self.fare}")
        print(f"The seats of the Train is {self.seats}")
    def getTickets(self):
        if(self.seats>0):
            print(f"Your ticket has been booked !! and your seat number is {self.seats}")
            self.seats=self.seats-1
        else:
            print("Sorry !! Train is fully booked ")
Shantanu=Train("Tapovan Express : 173205",700,2)
Shantanu.getStatus()
Shantanu.getTickets()
Shantanu.getStatus()
Shantanu.getTickets()
Shantanu.getStatus()
Shantanu.getTickets()