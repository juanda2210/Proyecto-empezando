from data import load_data, save_data

def registrar_trainer():
    data = load_data()

    trainer = {
        "id" : input("Numero de documento del trainer:"),
        "nombre": input("nombre: "),
        "apellido": input("apellido: "),
        "rutas": input("Define ruta Java,Netcore,NodeJS: "),
        "usuario": (""),
        "contrasena" : (""),
        "horario": (""),              
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