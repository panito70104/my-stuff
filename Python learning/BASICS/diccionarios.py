def info_auto():
    auto = {
        "marca": "Toyota",
        "modelo": "Corolla",
        "año": 2020,
    }
    auto["año"] = 2022
    auto["color"] = "rojo"
    del auto["modelo"]
    print(auto)
info_auto()