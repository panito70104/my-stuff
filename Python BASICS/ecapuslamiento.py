class cajafuerte:
    def __init__(self, contenido):
        self.__contenido = contenido

    def agregar(self, objeto):
        self.__contenido.append(objeto)

    def mostrar_contenido(self):
        print("Contenido de la caja fuerte:")
        for objeto in self.__contenido:
            print(objeto)
#uso caja_fuerte
cuenta = cajafuerte([])

cuenta.agregar("Dinero")
cuenta.agregar("Joyas")
cuenta.agregar("Documentos importantes")
cuenta.mostrar_contenido()