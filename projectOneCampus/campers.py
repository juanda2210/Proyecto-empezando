from data import load_data, save_data

def registrar_camper ():
    data = load_data()
    print("Selecciona un horario")
    print("---------------------")
    print("1. 6 am a 2 pm")
    print("2. 10 am a 6 pm")
    print("")
    seleccion = int(input(": "))
    if seleccion == 1:
        horario = "6 am a 2 pm"
    elif seleccion == 2:
        horario = "10 am a 6 pm"    
    camper = {
        "id" : input("ID: "),
        "nombre" : input("Nombre: "),
        "apellido" : input("Apellido: "),
        "direccion" : input("Direccion: "),
        "acudiente" : input("Nombre acudiente: "),
        "telefono_cel" : input("Numero de telefono celular: "),
        "horario" : horario,
        "estado" : "Inscrito",
        "riesgo" : "",
        "notas" : {}
    }

    data ["campers"].append(camper)
    save_data(data)
    print("")
    print("Camper registrado correctamente")

def actualizar_estado():
    data = load_data()
    buscarID = input("Ingrese el ID o documento del camper: ")

    for camper in data["campers"]:
        if camper["id"] == buscarID:
            camper["estado"] = "Aprobado"

    save_data(data)
    print("")
    print("Estado actualizado correctamente")        
