class NodoBST:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBst: # Clase para representar un árbol binario de búsqueda
    def __init__(self):
        self.raiz = None

    def insertar(self, valor): # Método para insertar un nuevo valor en el árbol
        nuevo = NodoBST(valor)
        if self.raiz is None:
            self.raiz = nuevo
            return
        actual = self.raiz
        while True:
            if valor < actual.valor:
                if actual.izquierda is None:
                    actual.izquierda = nuevo
                    return
                actual = actual.izquierda
            elif valor > actual.valor:
                if actual.derecha is None:
                    actual.derecha = nuevo
                    return
                actual = actual.derecha
            else:
                return
            #print(valor, "se ha añadido a tu lista de contactos")
    def buscar(self, valor): # Método para buscar un valor en el árbol
        actual = self.raiz
        while actual is not None:
            if valor == actual.valor:
                print(valor, "Si esta en tu lista de contactos")
                return True
            elif valor < actual.valor:
                actual = actual.izquierda
            else:
                actual = actual.derecha
        print(valor, "No esta en tu lista de contactos")
        return False

    def eliminar(self, valor): # Método para eliminar un valor del árbol
        actual = self.raiz
        padre = None
        while actual is not None and actual.valor != valor:
            padre = actual
            if valor < actual.valor:
                actual = actual.izquierda
            else:
                actual = actual.derecha
        if actual is None:
            return  # No encontrado

        print(valor, "Ha sido elimiando de tu lista de contactos")


        if actual.izquierda is None and actual.derecha is None:
            if padre is None:
                self.raiz = None
            elif padre.izquierda == actual:
                padre.izquierda = None
            else:
                padre.derecha = None

        # Caso 2: Nodo con un hijo
        elif actual.izquierda is None or actual.derecha is None:
            hijo = actual.izquierda if actual.izquierda else actual.derecha
            if padre is None:
                self.raiz = hijo
            elif padre.izquierda == actual:
                padre.izquierda = hijo
            else:
                padre.derecha = hijo

        # Caso 3: Nodo con dos hijos
        else:
            sucesor_padre = actual
            sucesor = actual.derecha
            while sucesor.izquierda:
                sucesor_padre = sucesor
                sucesor = sucesor.izquierda
            actual.valor = sucesor.valor
            if sucesor_padre.izquierda == sucesor:
                sucesor_padre.izquierda = sucesor.derecha
            else:
                sucesor_padre.derecha = sucesor.derecha

    def imprimir_inorden(self):
        actual = self.raiz
        stack = []
        while True:
            while actual is not None:
                stack.append(actual)
                actual = actual.izquierda
            if not stack:
                break
            actual = stack.pop()
            print(actual.valor)
            actual = actual.derecha

arbol = ArbolBst()
arbol.insertar("Kevin")
arbol.insertar("Luis")
arbol.insertar("Carlos")
arbol.insertar("Andres")
arbol.insertar("Jorge")
arbol.insertar("Pedro")
arbol.insertar("Juan")
arbol.insertar("Diego")
arbol.insertar("Javier")
arbol.insertar("Fernando")
arbol.imprimir_inorden()
arbol.buscar("Kevin")
arbol.buscar("Elder")
arbol.eliminar("Kevin")