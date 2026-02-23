from campers import registrar_camper, actualizar_estado, actualizar_informacion, usu_contra, login_camper
from trainers import registrar_trainer, usuario_contrasena, login_trainer
from asistencias import asistencia, eliminar_asistencia
from asistencias import inasistencia, eliminar_inasistencia
from asistencias import retardo, eliminar_retardo
from asistencias import inasistencia_justificada, eliminar_inasistencia_justificada
from puntos import puntos_positivos, puntos_negativos
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
    menuPrincipal = int(input("Seleccione la opción con la que desea ingresar: "))

    if menuPrincipal == 1:
        print("Bienvenido(a) al portal de Coordinador de Campuslands")
        print("-----------------------------------------------------")
        usuarioIngresado = input("Ingresa tu usuario: ")
        if (usuarioIngresado.strip().lower() == usuarioCoordinador.strip().lower()):
            contraseñaIngresada = input("Ingresa tu contraseña: ")
            if (contraseñaIngresada == contraseñaCoordinador):
                refDos = True
                while refDos == True:
                    print("---------------------------------Funcionalidades-------------------------------------")
                    print("1. Registro de estudiantes")
                    print("2. Registro de trainers")
                    print("3. Asistencias")
                    print("4. Modificación de datos personales")
                    print("5. Sistema de puntos positivos y negativos")
                    print("6. Sistema de notas")
                    print("7. Registrar a un estudiante como aprobado e ingreso a grupo")
                    print("8. Reportes")
                    print("9. Asignar correos y contraseñas")
                    print("10. Salir a menu principal")
                    menuCoordinador = int(input("digite la funcionalidad a la que desea entrar: "))
                    if menuCoordinador == 1:
                        print("Sistema de registro de estudiantes")
                        print("----------------------------------")
                        registrar_camper()
                    elif menuCoordinador == 2:
                        print("Sistema de registro de trainer")
                        registrar_trainer()
                    elif menuCoordinador == 3:
                        print("Sistema de asistencias de campuslands")
                        print("-------------------------------------")
                        print("1. Registrar asistencia")
                        print("2. Registrar inasistencia")
                        print("3. Registrar retardo")
                        print("4. Registrar inasistencia justificada")
                        print("5. Eliminar asistencia")
                        print("6. Eliminar inasistencia")
                        print("7. Eliminar retardo")
                        print("8. Eliminar inasistencia justificada")
                        opcion = int(input(": "))
                        if opcion == 1:
                            asistencia()
                        elif opcion == 2:
                            inasistencia()
                        elif opcion == 3:
                            retardo()
                        elif opcion == 4:
                            inasistencia_justificada()
                        elif opcion == 5:
                            eliminar_asistencia()
                        elif opcion == 6:
                            eliminar_inasistencia()
                        elif opcion == 7:
                            eliminar_retardo()
                        elif opcion == 8:
                            eliminar_inasistencia_justificada()      
                    elif menuCoordinador == 4:
                        print("Sistema de modificacion de datos personales")
                        print("-------------------------------------------")
                        actualizar_informacion()
                    elif menuCoordinador == 5:
                        print("Sistema de puntos positivos y negativos")
                        print("---------------------------------------")
                        print("1. Digitar punto positivos")
                        print("2. Digitar punto negativo")
                        opcion = int(input(": "))
                        if opcion == 1:
                            puntos_positivos()
                        elif opcion == 2:
                            puntos_negativos()    
                    elif menuCoordinador == 6:
                        print("Sistema de notas")   
                    elif menuCoordinador == 7:
                        print("Cambio de estado")
                        print("----------------")
                        actualizar_estado()
                    elif menuCoordinador == 8:
                        print("Sistema de reportes")
                    elif menuCoordinador == 9:
                        menuDeAsignacionDeCorreos = True
                        while menuDeAsignacionDeCorreos == True:
                            print(".\Menu de asignacion de correos y contraseñas")
                            print("-------------------------------------------")
                            print("1. campers")
                            print("2. trainers")
                            print("3. salir a menu de coordina1dor")
                            opcion = int(input(": "))
                            if opcion == 1: 
                                usu_contra()
                            elif opcion == 2:
                                usuario_contrasena()
                            elif opcion == 3:
                                menuDeAsignacionDeCorreos = False        
                    elif menuCoordinador == 10:
                        refDos = False
    elif menuPrincipal == 2: 
        print("Bienvenido(a) al portal de campers")
        print("-----------------------------------")
        camper_logueado = login_camper()
        if camper_logueado:
            print("Acceso concedido")
            print("Nombre:", camper_logueado["nombre"])
            print("Grupo:", camper_logueado.get("grupo"))
            print("------------------------------------------------")
            print("Bienvenido(a) al portal de camper de Campuslands")
            print("------------------------------------------------")
            print("")
            print("----------------Funcionalidades-----------------")
            print("1. Revisar notas")
            print("2. Revisar mis asistencias")
        else:
            print("No se pudo iniciar sesión")
    elif menuPrincipal == 3:
        print("Bienvenido(a) al portal de trainer de Campuslands")
        print("-------------------------------------------------")
        trainer_logueado = login_trainer()
        if trainer_logueado:
            print("Acceso concedido al menú trainer")
            print("Bienvenido(a) al portal de trainer de Campuslands")
            print("-------------------------------------------------")
            print("")
            print("----------------Funcionalidades------------------")
            print("1. Modificación de notas")
            print("2. Revisar datos generales de los campers")
        else:
            print("No se pudo iniciar sesión")
    elif menuPrincipal == 4:
        print("Gracias por navegar con nosotros")
        refUno = False