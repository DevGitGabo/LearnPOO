# Esta es una clase con atributos.

class Hotel:
    def __init__(self, num_guests, parking_spaces):
        self.num_guests = num_guests
        self.parking_spaces = parking_spaces
        self.guests = 0

# Para añadir métodos.

    def add_guests(self, num_guests):
        self.guests += num_guests

    def checkout(self, num_guests):
        self.guests -= num_guests

    def total_occupancy(self):
        return self.guests

hotel = Hotel(50,20)
hotel.add_guests(3)
hotel.checkout(1)
hotel.total_occupancy() #2



