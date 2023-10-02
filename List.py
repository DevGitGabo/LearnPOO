# Lo que se haría sin POO.

cuartos_de_hotel = [101, 102, 103, 201, 202, 203]
cuarto_ocupado = [True, False, False, True, True, False]

# Con POO.

# Esto es una creación de una clase.
class Hotel:
    pass

# En el contexto de la clase Hotel, pass se utiliza para indicar que la clase está vacía por el momento, 
# pero se espera que tenga definiciones de atributos y métodos en el futuro. 

# Esto es una instancia de la clase.
hotel = Hotel()

class Hotel:
    def __init__(self, num_guests, parking_spaces):
        self.num_guests = num_guests
        self.parking_spaces = parking_spaces
        self.guests = 0

hotel = Hotel(num_guests=50,parking_spaces=20)
print(hotel.parking_spaces) # 20

