def editar_lista_de_frutas():
    frutas = ["manzana", "pera", "sandia", "melon"]
    print(frutas)
    frutas[1] = "kiwi"
    print(frutas)
    frutas.remove("melon") #Eliminar por valor
    print(frutas)
    frutas.append("mango")
    frutas.append("piña")
    print(frutas)
    del frutas[0] #Eliminar por indice
    print(frutas)
    for fruta in frutas:
        print(fruta)
    print(len(frutas))
editar_lista_de_frutas()
