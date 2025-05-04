class Vehiculo:
    def __init__(self, marca, año):
        self.marca = marca
        self.año = año
class Coche(Vehiculo):
    def carro (self):
        print(f"Soy un coche de la marca {self.marca} y del año {self.año}")

class Moto(Vehiculo):
    def moto (self):
        print(f"Soy una moto de la marca {self.marca} y del año {self.año}")

class Camion(Vehiculo):
    def camion(self):
        print(f"Soy un camion de la marca {self.marca} y de año {self.año}")
ca = Camion("Mercedes", 2021)        
c = Coche("Toyota", 2020)
m = Moto("Yamaha", 2019)

c.carro()
m.moto()
ca.camion()