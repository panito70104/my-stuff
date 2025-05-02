class auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}")
x = auto("Toyota", "Corolla", 2020)
y = auto("Mazda", "CX-5", 2021)
z = auto("Tesla", "Cybertruck", 2022)

x.mostrar_info()
y.mostrar_info()
z.mostrar_info()