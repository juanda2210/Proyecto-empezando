from campers import registrar_camper 
from campers import actualizar_estado
from campers import actualizar_informacion
from campers import usu_contra
from trainers import registrar_trainer
from trainers import usuario_contrasena
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
                    print("4. Asignación de grupos")
                    print("5. Modificación de datos personales")
                    print("6. Sistema de puntos positivos y negativos")
                    print("7. Sistema de notas")
                    print("8. Registrar a un estudiante como aprobado o inscrito")
                    print("9. Crear notas de entrenamiento en el ingreso")
                    print("10. Rutas de entrenamiento")
                    print("11. Reportes")
                    print("12. Asignar correos y contraseñas")
                    print("13. Salir a menu principal")
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
                    elif menuCoordinador == 4:
                        print("Sistema de asignación de grupos")        
                    elif menuCoordinador == 5:
                        print("Sistema de modificacion de datos personales")
                        print("-------------------------------------------")
                        actualizar_informacion()
                    elif menuCoordinador == 8:
                        print("Cambio de estado")
                        print("----------------")
                        actualizar_estado()
                    elif menuCoordinador == 12:
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
                    elif menuCoordinador == 13:
                        refDos = False
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
    elif menuPrincipal == 4:
        print("Gracias por navegar con nosotros")
        refUno = False