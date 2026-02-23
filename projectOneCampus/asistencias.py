from data import load_data, save_data

def asistencia():
    data = load_data()

    buscarID = input("Ingrese el ID o documento del camper: ")
    for camper in data["campers"]:
        if camper["id"] == buscarID:
            if "asistencia" not in camper:
                camper["asistencia"] = 0
            camper["asistencia"] += 1
        break
    save_data (data)    

def inasistencia():
    data = load_data()

    buscarID = input("Ingrese el ID o documento del camper: ")
    for camper in data["campers"]:
        if camper["id"] == buscarID:
            if "inasistencia" not in camper:
                camper["inasistencia"] = 0
            camper["inasistencia"] += 1
        break

    save_data (data)   

def retardo():

    data = load_data()

    buscarID = input("Ingrese el ID o documento del camper: ")
    for camper in data["campers"]:
        if camper["id"] == buscarID:
            if "retardo" not in camper:
                camper["retardo"] = 0
            camper["retardo"] += 1
        break

    save_data (data)
        
def inasistencia_justificada():

    data = load_data()

    buscarID = input("Ingrese el ID o documento del camper: ")
    for camper in data["campers"]:
        if camper["id"] == buscarID:
            if "justificada" not in camper:
                camper["justificada"] = 0
            camper["justificada"] += 1
        break

    save_data (data)

def eliminar_asistencia():
    data = load_data()

    buscarID = input("Ingrese el ID o documento del camper: ")
    for camper in data["campers"]:
        if camper["id"] == buscarID:
            if "asistencia" not in camper:
                print("El camper aun no tiene asistencias")
            else:
                camper["asistencia"] -= 1
        break
    save_data (data)    

def eliminar_inasistencia():
    data = load_data()

    buscarID = input("Ingrese el ID o documento del camper: ")
    for camper in data["campers"]:
        if camper["id"] == buscarID:
            if "inasistencia" not in camper:
                print("El camper aun no tiene inasistencias")
            else:
                camper["inasistencia"] -= 1
        break

    save_data (data)   

def eliminar_retardo():

    data = load_data()

    buscarID = input("Ingrese el ID o documento del camper: ")
    for camper in data["campers"]:
        if camper["id"] == buscarID:
            if "retardo" not in camper:
                print("El camper aun no tiene retardos")
            else:
                camper["retardo"] -= 1
        break

    save_data (data)
        
def eliminar_inasistencia_justificada():

    data = load_data()

    buscarID = input("Ingrese el ID o documento del camper: ")
    for camper in data["campers"]:
        if camper["id"] == buscarID:
            if "justificada" not in camper:
                print("El camper aun no tiene inasistencias justificadas")
            else:
                camper["justificada"] -= 1
        break

    save_data (data)