from data import load_data, save_data

def registrar_camper ():
    data = load_data()
    print("Selecciona un horario")
    print("---------------------")
    print("1. 6 am a 2 pm")
    print("2. 10 am a 6 pm")
    print("3. 2 pm a 10 pm")
    print("")
    seleccion = int(input(": "))
    if seleccion == 1:
        horario = "6 am a 2 pm"
    elif seleccion == 2:
        horario = "10 am a 6 pm"    
    elif seleccion == 3:
        horario = "2 pm a 6 pm"    
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
        "usuario" : (""),
        "contrasena": (""),
        "grupo" : ""

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
            for grupo in data["grupos"]:
                if len(grupo["nombres"]) < 35:
                    grupo["nombres"].append(camper["nombre"])
                    grupo["apellidos"].append(camper["apellido"])
                    grupo["id"].append(camper["id"])
                    camper["grupo"] = grupo["titulo"]
                    print("Camper agregado al grupo ",grupo["titulo"])
                    break

    save_data(data)
    print(".\Estado actualizado correctamente")

def actualizar_informacion():
    data = load_data()
    buscarID = input("Ingrese el ID del camper: ")

    for camper in data["campers"]:
        if camper["id"] == buscarID:

            print("\n¿Qué dato desea actualizar?")
            print("1. Nombre")
            print("2. Apellido")
            print("3. Dirección")
            print("4. Acudiente")
            print("5. Teléfono")
            print("6. Horario")

            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                camper["nombre"] = input("Nuevo nombre: ")
            elif opcion == 2:
                camper["apellido"] = input("Nuevo apellido: ")
            elif opcion == 3:
                camper["direccion"] = input("Nueva dirección: ")
            elif opcion == 4:
                camper["acudiente"] = input("Nuevo acudiente: ")
            elif opcion == 5:
                camper["telefono_cel"] = input("Nuevo teléfono: ")
            elif opcion == 6:
                print("Seleccione nuevo horario")
                print("1. 6 am a 2 pm")
                print("2. 10 am a 6 pm")
                print("3. 2 pm a 6 pm")
                seleccion = int(input(": "))

                if seleccion == 1:
                    camper["horario"] = "6 am a 2 pm"
                elif seleccion == 2:
                    camper["horario"] = "10 am a 6 pm"
                elif seleccion == 3:
                    camper["horario"] = "2 pm a 10 pm"
                
    save_data(data)
    print("\nDato actualizado correctamente")    

def usu_contra():
    data = load_data()

    buscarID = input("Numero de documento de identidad: ")
    
    for campers in data["campers"]:
        if campers["id"] == buscarID:
            usuario = input("usuario: ")
            contrasena = input("contraseña: ")
            campers["usuario"] = usuario
            campers["contrasena"] = contrasena
 
    save_data(data)
    print("\nusuario y contraseña guardados exitosamente")           

def login_camper():
    data = load_data()

    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")

    for camper in data["campers"]:
        if camper.get("usuario") == usuario and camper.get("contrasena") == contrasena:
            print("Ingreso exitoso. Bienvenido", camper["nombre"])
            return camper 

    print("Usuario o contraseña incorrectos.")
    return None