class NodoBST:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
class Arbol_Bst:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor): # Método para insertar un valor en el árbol
        if self.raiz is None:
            self.raiz = NodoBST(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor): # Método auxiliar para insertar un valor de forma recursiva
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = NodoBST(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            if nodo.derecha is None:
                nodo.derecha = NodoBST(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo.derecha, valor)

    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return nodo
        if valor < nodo.valor:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, valor)
        else:
            # Nodo con un solo hijo o sin hijos
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            # Nodo con dos hijos: obtener el sucesor inorden
            temp = self._min_valor_nodo(nodo.derecha)
            nodo.valor = temp.valor
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, temp.valor)
        return nodo

    def _min_valor_nodo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    def imprimir_inorden(self):
        self._imprimir_inorden_recursivo(self.raiz)

    def _imprimir_inorden_recursivo(self, nodo):
        if nodo is not None:
            self._imprimir_inorden_recursivo(nodo.izquierda)
            print(nodo.valor)
            self._imprimir_inorden_recursivo(nodo.derecha)

arbol = Arbol_Bst() # Crear una instancia del árbol binario de búsqueda
arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(15)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(12)
arbol.insertar(20)
arbol._imprimir_inorden_recursivo(arbol.raiz)
arbol.buscar(7)
arbol.eliminar(5)
arbol._imprimir_inorden_recursivo(arbol.raiz)
