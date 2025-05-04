class nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
class lista_Enalzada:
    def __init__(self):
        self.cabeza = None
    
    def agregar(self, valor):
        nuevo_nodo = nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        
    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")


lista = lista_Enalzada()
lista.agregar("A")
lista.agregar("B")
lista.agregar("C")
lista.mostrar()