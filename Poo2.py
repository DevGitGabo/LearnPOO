class Hotel:
    def __init__(self, num_guests, parking_spaces):
        self.num_guests = num_guests
        self.parking_spaces = parking_spaces
        self.guests = 0

hotel = Hotel(num_guests=50,parking_spaces=20)
print(hotel.parking_spaces) # 20