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

def login_trainer():
    data = load_data()

    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")

    for trainer in data["trainers"]:
        if trainer.get("usuario") == usuario and trainer.get("contrasena") == contrasena:
            print("Ingreso exitoso. Bienvenido", trainer["nombre"])
            return trainer

    print("Usuario o contraseña incorrectos.")
    return None

def asignar_notas(trainer):
    data = load_data()

    print("Trainer:", trainer["nombre"])
    gruposTrainer = trainer.get("grupos", [])
    
    print("¿A qué grupo deseas asignar notas?")
    
    for i, grupo in enumerate(gruposTrainer, start=1):
        print(f"{i}. Grupo {grupo}")

    print("-------------------")
    opcion = int(input("Seleccione una opción: "))

    if 1 <= opcion <= len(gruposTrainer):
        grupoSeleccionado = gruposTrainer[opcion - 1]
        print("Has seleccionado el grupo: ", grupoSeleccionado)

        for grupo in data["grupos"]:
            if grupo["titulo"] == grupoSeleccionado:

                nombres = grupo.get("nombres", [])
                apellidos = grupo.get("apellidos", [])

                if not nombres:
                    print("Este grupo no tiene estudiantes.")
                    return

                print("\nEstudiantes del grupo:\n")

                for i in range(len(nombres)):
                    print(f"{i+1}. {nombres[i]} {apellidos[i]}")
                
                print("\nSeleccione el estudiante:")
                estOpcion = int(input("Opción: "))

                if 1 <= estOpcion <= len(nombres):
                    estudiante_id = grupo["id"][estOpcion - 1]
                else:
                    print("Opción inválida.")
                    return
                
                print("-------------------------------------")
                print("\nSeleccione la ruta: ")
                print("1. Fundamentos de programación")
                print("2. Programación Web")
                print("3. Programación formal")
                print("4. Bases de datos")
                print("5. Backend")

                op_materia = int(input("Opción: "))

                if op_materia == 1:
                    nombreRuta = "nota_fundamentos_de_programacion"
                elif op_materia == 2:
                    nombreRuta = "nota_programacion_web"
                elif op_materia == 3:
                    nombreRuta = "nota_programacion_formal"
                elif op_materia == 4:
                    nombreRuta = "nota_bases_de_datos"
                elif op_materia == 5:
                    nombreRuta = "nota_backend"
                else:
                    print("Opción inválida.")
                    return
                
                print("----------------------------------------")
                for camper in data["campers"]:
                    if camper["id"] == estudiante_id:

                        if nombreRuta in camper:
                            print("Este estudiante ya tiene nota en esta materia.")
                            return

                        nota = float(input("Ingrese la nota: "))

                        camper[nombreRuta] = nota

                        save_data(data)

                        print("Nota asignada correctamente.")
                        return

                break
    else:
        print("Opción inválida.")

def mostrar_estudiante():
    data = load_data()

    print("Digite el numero de id del estudiante: ")
    idCap = input(": ")

    for camper in data["campers"]:
        if idCap == camper["id"]:
            print("\nEstudiante encontrado:")
            print("Nombre:", camper["nombre"], camper["apellido"])
            print("\nNotas:")

            print("Fundamentos de programación:", camper.get("nota_fundamentos_de_programacion", "Sin nota"))
            print("Programación Web:", camper.get("nota_programacion_web", "Sin nota"))
            print("Programación formal:", camper.get("nota_programacion_formal", "Sin nota"))
            print("Bases de datos:", camper.get("nota_bases_de_datos", "Sin nota"))
            print("Backend:", camper.get("nota_backend", "Sin nota"))

            return

    print("Estudiante no encontrado.")