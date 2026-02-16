from data import load_data, save_data

def registrar_camper ():
    data = load_data()
    camper = {
        "id" : input("ID: "),
        "nombre" : input("Nombre: "),
        "apellido" : input("Apellido: "),
        "direccion" : input("Direccion: "),
        "acudiente" : input("Nombre acudiente: "),
        "telefono_cel" : input("Numero de telefono celular: "),
        "estado" : "Inscrito",
        "riesgo" : "",
        "notas" : {}
    }

    data ["campers"].append(camper)
    save_data(data)
    print("")
    print("Camper registrado correctamente")