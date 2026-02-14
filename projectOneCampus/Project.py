usuarioCoordinador = "coordinadorcampus"
contraseñaCoordinador = "campus123"
refUno = True
while refUno == True :
    print("Bienvenido(a) al portal de campuslands")
    print("--------------------------------------")
    print("")
    print("-----------1. Coordinador-------------")
    print("-------------2. Camper----------------")
    print("------------3. Trainer----------------")
    print("-------------4. Salir-----------------")
    print("")
    menuPrincipal = input("Seleccione la opción con la que desea ingresar: ")

    if menuPrincipal == 1:
        print("Bienvenido(a) al portal de Coordinador de Campuslands")
        print("-----------------------------------------------------")
        print("")
        usuarioIngresado = input("Ingresa tu usuario: ")
        if (usuarioIngresado.strip().lower() == usuarioCoordinador.strip().lower()):
            contraseñaIngresada = input("Ingresa tu contraseña: ")
            if (contraseñaIngresada == contraseñaCoordinador):
                print("-------Funcionalidades---------")
                print("1. Registro de estudiantes")
                print("2. Asistencias")
                print("3. Asignación de horarios")
                print("4. Modificación de datos personales")
                print("5. Sistema de puntos positivos y negativos")
                print("6. Sistema de notas")
                print("7. Registrar a un estudiante como aprobado o no aprobado")
                print("8. Crear notas de entrenamiento en el ingreso")
                print("9. Rutas de entrenamiento")
                print("10 Reportes")

    elif menuPrincipal == 2: 
        print("Bienvenido(a) al portal de camper de Campuslands")
        print("------------------------------------------------")
        print("")
        print("----------------Funcionalidades-----------------")
        print("1. Revisar notas")
        print("2. Subir trabajos")
        print("3. Realizar examenes")
        print("4. Revisar el horario")
        print("5. Toma de asistencia")
    elif menuPrincipal == 3:
        print("Bienvenido(a) al portal de trainer de Campuslands")
        print("-------------------------------------------------")
        print("")
        print("----------------Funcionalidades------------------")
        print("1. Modificación de notas")
        print("2. Subir material para trabajos")
        print("3. Revisión de trabajos entregados por estudiantes")
        print("4. Poner exámenes")
        print("5. Revisar datos generales de los campers")
        print("6. Asistencia en la parte académica")
        print("7. Procesos disciplinarios")