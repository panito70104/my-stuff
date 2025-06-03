import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel("ventas_vendedores.xlsx")
print(data.columns)  # <-- Agrega esta línea para ver los nombres de las columnas
def sumar_ventas_por_vendedor(data): #sum of sells by seller
    for vendedor in data["Vendedor"].unique():
        suma = data[data["Vendedor"] == vendedor]["Ventas"].sum() #sum sales
        print(f"{vendedor}: {suma}")

def medias_por_vendedor(data): #average of sells by seller
    for vendedor in data["Vendedor"].unique():
        media = data[data["Vendedor"] == vendedor]["Ventas"].mean() #average sales
        print(f"{vendedor}: {media}")

def best_seller(data): #best seller
    best = data.groupby("Vendedor")["Ventas"].sum().idxmax() #find the seller with the most sales
    print(f"El mejor vendedor es: {best}")

def month_biggest_sell(data):  # month with the most sales
    meses = {
        "Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4,
        "Mayo": 5, "Junio": 6, "Julio": 7, "Agosto": 8,
        "Septiembre": 9, "Octubre": 10, "Noviembre": 11, "Diciembre": 12
    }
    data["Mes_num"] = data["Mes"].map(meses)
    mes_mayor_venta = data.groupby("Mes_num")["Ventas"].sum().idxmax()
    # Para mostrar el nombre del mes:
    mes_nombre = [k for k, v in meses.items() if v == mes_mayor_venta][0]
    print(f"El mes con mayor venta es: {mes_nombre}")

def graficar_ventas_por_vendedor(data): #graph sales by seller
    ventas_por_vendedor = data.groupby("Vendedor")["Ventas"].sum() #group sales by seller
    ventas_por_vendedor.plot(kind='bar') #plot bar chart
    plt.title("Ventas por Vendedor")
    plt.xlabel("Vendedor")
    plt.ylabel("Ventas")
    plt.show()

def seller_upper_than_1000(data): #sellers with sales greater than 1000
    for vendedor in data["Vendedor"].unique():
        suma = data[data["Vendedor"] == vendedor]["Ventas"].sum()
        if suma > 25000:
            print(f"{vendedor}: {suma}")

sumar_ventas_por_vendedor(data)
medias_por_vendedor(data)
best_seller(data)
month_biggest_sell(data)
graficar_ventas_por_vendedor(data)
seller_upper_than_1000(data)