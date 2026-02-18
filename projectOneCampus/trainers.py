from data import load_data, save_data

def registrar_trainer():
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
        horario = "2 pm a 10 pm"    
    trainer = {

        "id" : input("Numero de documento del trainer:"),
        "nombre": input("nombre: "),
        "apellido": input("apellido: "),
        "rutas": input("Define ruta Java,Netcore,NodeJS: "),
        "usuario": (""),
        "contrasena" : (""),
        "horario": horario,              
        "grupos" : input("Grupos: ")
    }

    data["trainers"].append(trainer)
    save_data(data)
    print("Trainer registrado.")

def usuario_contrasena():
    data = load_data()

    buscarID = input("Numero de documento de identidad: ")

    for trainer in data ["trainers"]:
        if trainer["id"] == buscarID:
            usuario = input("usuario: ")
            contrasena = input("contraseña: ")
            trainer["usuario"] = usuario
            trainer["contrasena"] = contrasena  
    
    save_data(data)
    print(".\Correo y contraseña guardados exitosamente")