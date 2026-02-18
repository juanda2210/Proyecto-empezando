from data import load_data, save_data

def puntos_positivos():
    data = load_data

    buscarID = input("Numero de documento del camper: ")
    for camper in data["campers"]:
        if camper["id"] == buscarID:
            if "puntos positivos" not in camper:
                camper["puntos positivos"] = 0
            camper["puntos positivos"] += 1

    save_data(data)            

def puntos_negativos():
    data = load_data

    buscarID = input("Numero de documento del camper: ")
    for camper in data["campers"]:
        if camper["id"] == buscarID:
            if "puntos negativos" not in camper:
                camper["puntos negativos"] = 0
            camper["puntos negativos"] += 1

    save_data(data)  