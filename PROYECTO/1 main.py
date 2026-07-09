from calculos_generales import *
from config import *
from diccionario_juegos import *
from diccionarios import *
from estadisticas import *
from funciones_dict import *
from input import *
from mostrar_estadisticas import *
from reglas_dict import *
from validaciones import *
from zzz_test import *

while True:
    print("""\n= MENÚ ========================================================================================================================\n""")
    if dict_acumuladores[0]["cantidad_usuarios"] == 0:
        opcion = pedir_entero(menu_2, r + "ERROR. " + rs + "Debe ser un número del 1 al 4. Ingrese una opción: ")

        while not validar_rango(opcion, 1, 4) or (opcion == 2 or opcion == 3):
            if (opcion == 2 or opcion == 3):
                print(r + "ERROR. " + rs + "Primero debe ingresar al menos un usuario.")
            else:
                print(r + "ERROR. " + rs + "Debe ser un número del 1 al 4.")

            opcion = pedir_entero(menu_2, "Ingrese una opción: ")
    else:
        opcion = pedir_entero(menu, "Ingrese una opción: ")

        while not validar_rango(opcion, 1, 4):
            print(r + "ERROR. " + rs + "Debe ser un número del 1 al 4.")
            opcion = pedir_entero(menu, "Ingrese una opción: ")

    lista_estadisticas_generales[0]["flag_case2"] = True

    match opcion:
        case 1:
            #region ENTRADAS
            print("""\n= ENTRADAS =====================================================================================================================\n""")
            nombre = pedir_cadena("Ingrese su nombre: ", r + "ERROR. " + rs + "Ingrese su nombre solo usando letras: ")
            
            usuario_encontrado = buscar_usuario(lista_usuarios, nombre) #preguntar profe variable suelta
            
            mensaje_error = r + "ERROR. " + rs + "Ingrese una opcion válida " + m + "[Si / No]" + rs + ": "
            if usuario_encontrado > -1:
                opcion = pedir_cadena("Esta ingresando a " + m + f"'{nombre}'" + rs + ", usuario ya existente. ¡Los datos se reemplazaran por los nuevos! ¿Desea continuar? " + m + "[Si / No]" + rs + ": ", mensaje_error, True)
                while validar_cadena(opcion, "si", "no") == False:
                    opcion = pedir_cadena(mensaje_error, mensaje_error, True)
                if opcion == "si":
                    pass
                else:
                    continue

            print("Bienvenid@ " + m + f"{nombre}" + rs + " al sistema de recomendación de videojuegos, lindo nombre" + y + " ☺︎")
            print(rs + "A continuación le pediremos que ingrese algunos datos.")

            juego_favorito = input("Ingrese su juego favorito: ")

            mensaje_error = r + "ERROR. " + rs + "Ingrese una edad válida solo usando números" + m + " (Minímo 8 años, máximo 100)" + rs + ": " 
            edad = pedir_entero("Ingrese su edad: ", mensaje_error)
            while validar_rango(edad, 8, 100) == False:
                edad = pedir_entero(r + "ERROR. " + rs + "Ingrese una edad válida" + m + " (Minímo 8 años, máximo 100)" + rs + ": ", mensaje_error)

            mensaje_error = r + "ERROR. " + rs + "Ingrese un genero valido " + m + "[Masculino / Femenino / No Binario]" + rs + ": "
            genero = pedir_cadena("Ingrese su genero " + m + "[Masculino / Femenino / No Binario]" + rs + ": ", mensaje_error, True)
            while validar_cadena(genero, "masculino", "femenino", "no binario") == False:
                genero = pedir_cadena(mensaje_error, mensaje_error, True)

            mensaje_error = r + "ERROR. " + rs + "Ingrese un genero valido " + m + "[Accion / Historia / Estrategia]" + rs + ": "
            genero_juego = pedir_cadena("Ingrese su genero de juegos favorito " + m + "[Accion / Historia / Estrategia]" + rs + ": ", mensaje_error, True)
            while validar_cadena(genero_juego, "accion", "historia", "estrategia") == False:
                genero_juego = pedir_cadena(mensaje_error, mensaje_error, True)

            mensaje_error = r + "ERROR. " + rs + "Ingrese un modo de juego valido " + m + "[Solo / Multijugador / Cooperativo]" + rs + ": "
            modo_de_juego = pedir_cadena("Ingrese su modo de juego preferido " + m + "[Solo / Multijugador / Cooperativo]" + rs + ": ", mensaje_error, True)
            while validar_cadena(modo_de_juego, "solo", "multijugador", "cooperativo") == False:
                modo_de_juego = pedir_cadena(mensaje_error, mensaje_error, True)

            if modo_de_juego == "solo":
                cantidad_de_amigos = 0

            mensaje_error = r + "ERROR. " + rs + "Ingrese una cantidad valida solo usando números " + m + "[Entre 0 y 15]" + rs + ": "
            if validar_cadena(modo_de_juego, "multijugador", "cooperativo") == True:
                cantidad_de_amigos = pedir_entero("Ingrese con cuantas personas mas va a jugar " + m + "[Entre 0 y 15]" + rs + ": ", mensaje_error)
                while validar_rango(cantidad_de_amigos, 0, 15) == False:
                    cantidad_de_amigos = pedir_entero(r + "ERROR. " + rs + "Ingrese una cantidad valida " + m + "[Entre 0 y 15]" + rs + ": ", mensaje_error)

            mensaje_error = r + "ERROR. " + rs + "Ingrese un perfil de jugador valido " + m + "[Casual / Competitivo]" + rs + ": "
            perfil_de_jugador = pedir_cadena("Ingrese su perfil de jugador " + m + "[Casual / Competitivo]" + rs + ": ", mensaje_error, True)
            while validar_cadena(perfil_de_jugador, "casual", "competitivo") == False:
                perfil_de_jugador = pedir_cadena(mensaje_error, mensaje_error, True)

            mensaje_error = r + "ERROR. " + rs + "Ingrese una plataforma valida " + m + "[Consola / PC]" + rs + ": "
            plataforma = pedir_cadena("Ingrese la plataforma en la que va a jugar " + m + "[Consola / PC]" + rs + ": ", mensaje_error, True)
            while validar_cadena(plataforma, "consola", "pc") == False:
                plataforma = pedir_cadena(mensaje_error, mensaje_error, True)

            mensaje_error = r + "ERROR. " + rs + "Ingrese una gama valida " + m + "[Baja / Media / Alta]" + rs + ": "
            if validar_cadena(plataforma, "pc") == True:
                gama = pedir_cadena("Ingrese la gama de su plataforma " + m + "[Baja / Media / Alta]" + rs + ": ", mensaje_error, True)
                while validar_cadena(gama, "baja", "media", "alta") == False:
                    gama = pedir_cadena(mensaje_error, mensaje_error, True)
            else:
                gama = "-"
            
            mensaje_error = r + "ERROR. " + rs + "Ingrese una cantidad mayor a 0 solo usando números" + rs + ": "
            espacio_disco = pedir_entero("Ingrese el espacio que tiene disponible en GB: ", mensaje_error)
            while validar_rango(espacio_disco, 1) == False:
                espacio_disco = pedir_entero(r + "ERROR. " + rs + "Ingrese una cantidad mayor a 0: ", mensaje_error)
            
            mensaje_error = r + "ERROR. " + rs + "Ingrese una cantidad de horas valida solo usando números " + m + "[Entre 0 y 24]" + rs + ": "
            horas = pedir_entero("Ingrese las horas que suele jugar al dia: ", mensaje_error)
            while validar_rango(horas, 0, 24) == False:
                horas = pedir_entero(r + "ERROR. " + rs + "Ingrese una cantidad de horas valida " + m + "[Entre 0 y 24]" + rs + ": ", mensaje_error)
            
            mensaje_error = r + "ERROR. " + rs + "Ingrese una cantidad no menor a 0 solo usando números: "
            presupuesto = pedir_entero("Ingrese su presupuesto en USD apróximado: ", mensaje_error)
            
            print("""\n===============================================================================================================================""")
            #endregion

            #region CALCULOS

            horas_semanales = horas * 7

            if validar_rango(horas_semanales, 0, 14):
                duracion = "corto"
            else:
                duracion = "largo"
    
            #PARA JUEGOS
            sumar_puntos(lista_juegos, "genero", genero_juego)
            sumar_puntos(lista_juegos, "modo_juego", modo_de_juego)
            sumar_puntos(lista_juegos, "perfil_jugador", perfil_de_jugador)
            sumar_puntos(lista_juegos, "edad", edad, "<=")
            sumar_puntos(lista_juegos, "duracion", duracion)
            
            if modo_de_juego != "solo":
                sumar_puntos(lista_juegos, "cant_amigos", cantidad_de_amigos, ">=")

            if plataforma == "pc":
                match gama:
                    case "baja":
                        gama_juego = 1
                    case "media":
                        gama_juego = 2
                    case "alta":
                        gama_juego = 3
                
                anular_puntos(lista_juegos, "gama", gama_juego, ">")

            elif plataforma == "consola":
                anular_puntos(lista_juegos, "plataforma", plataforma, "!=")

            anular_puntos(lista_juegos, "espacio_disco", espacio_disco, ">")
            anular_puntos(lista_juegos, "valor", presupuesto, ">")

            #endregion

            #region PUNTUACION

            recomendacion = []

            puntaje_maximo = lista_juegos[0]["puntos"]

            for juego in lista_juegos:
                puntaje_maximo = encontrar_maximo(juego["puntos"], puntaje_maximo)

            if puntaje_maximo != 0: #Esto significa que al menos hay una recomendacion
                for juego in lista_juegos:
                    if juego["puntos"] == puntaje_maximo:
                        recomendacion.append(juego["nombre"])
                        dict_acumuladores[0]["cantidad_recomendaciones"] += 1
#                        juego["frecuencia_recomendacion"] += 1

            if usuario_encontrado == -1:
                dict_acumuladores[0]["cantidad_usuarios"] += 1
                dict_acumuladores[0]["id_usuario"] += 1
                agregar_usuario(lista_usuarios, dict_acumuladores[0]["id_usuario"], nombre, edad, genero, juego_favorito,
                                genero_juego, modo_de_juego, cantidad_de_amigos, perfil_de_jugador,
                                plataforma, gama, espacio_disco, horas, presupuesto, recomendacion)
            else:

                modificar_usuario(lista_usuarios, usuario_encontrado, lista_usuarios[usuario_encontrado]["id_usuario"], nombre, edad, genero, juego_favorito,
                                genero_juego, modo_de_juego, cantidad_de_amigos, perfil_de_jugador,
                                plataforma, gama, espacio_disco, horas, presupuesto, recomendacion)
                
            mostrar_datos(nombre, juego_favorito, recomendacion, dict_acumuladores[0]["cantidad_recomendaciones"])

            anular_puntos(lista_juegos, "puntos", -1, "!=")
            #endregion
            
            #region SALIDAS
            #endregion
#            print("""\n===============================================================================================================================""")
        case 2:
            while lista_estadisticas_generales[0]["flag_case2"]:
                print("""\n= USUARIOS ===================================================================================================================\n""")
                print(f'Lista de usuarios ingresados "{dict_acumuladores[0]["cantidad_usuarios"]}": ')
                mostrar_usuarios(lista_usuarios)
                
                eleccion = pedir_entero("\nIngrese el ID del usuario que desea mostrar " + y + f"[{lista_usuarios[0]["id_usuario"]} - {lista_usuarios[-1]["id_usuario"]}]" + rs + ": ", r + "ERROR. " + rs + f"Debe ingresar un ID numerico " + y + f"[{lista_usuarios[0]["id_usuario"]} - {lista_usuarios[-1]["id_usuario"]}]" + rs + ": ")
                while validar_rango(eleccion, lista_usuarios[0]["id_usuario"], lista_usuarios[-1]["id_usuario"]) == False:
                    eleccion = pedir_entero(r + "ERROR. " + rs + "Ingrese un ID de usuario valido " + y + f"[{lista_usuarios[0]["id_usuario"]} - {lista_usuarios[-1]["id_usuario"]}]" + rs + ": ", r + "ERROR. " + rs + f"Debe ingresar un ID numerico " + y + f"[{lista_usuarios[0]["id_usuario"]} - {lista_usuarios[-1]["id_usuario"]}]" + rs + ": " )
                print("""\n===============================================================================================================================""")
                print("""= RESPUESTAS ==================================================================================================================""")
                for usuario in lista_usuarios:
                    if usuario["id_usuario"] == eleccion:
                        mostrar_usuario(usuario)
                        lista_estadisticas_generales[0]["flag_case2"] = False

                print("""===============================================================================================================================""")
        case 3:
            #region ESTADISTICAS
            print("""\n= ESTADISTICAS ===================================================================================================================\n""")
            sumar_puntos_si_son_iguales(lista_puntos_genero_juegos, lista_usuarios, "genero_juego", "Genero de juego", "puntos")
            establecer_puntos_lista_dict(lista_estadisticas_generales, "edad_maxima")
            establecer_puntos_lista_dict(lista_estadisticas_generales, "edad_minima", 101)
            establecer_puntos_lista_dict(lista_estadisticas_genero, "puntos")
            establecer_puntos_lista_dict(lista_estadisticas_genero, "presupuesto")
            establecer_puntos_lista_dict(lista_estadisticas_generales, "edad_maxima")
            establecer_puntos_lista_dict(lista_estadisticas_generales, "edad_minima", 101)
            establecer_puntos_lista_dict(lista_estadisticas_genero, "puntos")
            establecer_puntos_lista_dict(lista_estadisticas_genero, "presupuesto")
            establecer_puntos_lista_dict(dict_acumuladores, "usuarios_con_amigos")
            establecer_puntos_lista_dict(dict_acumuladores,"acumulador_edad")
            
            for usuario in lista_usuarios:
                dict_acumuladores[0]["acumulador_edad"] += usuario["Edad"]
                lista_estadisticas_generales[0]["edad_maxima"] = encontrar_maximo(usuario["Edad"], lista_estadisticas_generales[0]["edad_maxima"])
                lista_estadisticas_generales[0]["edad_minima"] = encontrar_minimo(usuario["Edad"], lista_estadisticas_generales[0]["edad_minima"])
                sumar_puntos(lista_estadisticas_genero, "genero", usuario["Genero"]) 
                sumar_puntos(lista_estadisticas_genero, "genero", usuario["Genero"], "==", "presupuesto", usuario["Presupuesto"])

                if usuario["Plataforma"] == "pc" and usuario["Gama"] == "alta":
                    lista_estadisticas_generales[0]["hay_pc_alta"] = True
                    dict_acumuladores[0]["max_presupuesto_pc_alta"] = encontrar_maximo(usuario["Presupuesto"], dict_acumuladores[0]["max_presupuesto_pc_alta"]) #Fijarnos si podemos poner que tambien muestre quien es el usuario con mayor pc presupuesto mayor..

                if usuario["Cantidad de amigos"] >= 1:
                    dict_acumuladores[0]["usuarios_con_amigos"] += 1

            for genero in lista_estadisticas_genero:
                            if genero["puntos"] > 0:
                                genero["promedio"] = promediar(genero["presupuesto"], genero["puntos"]) 
                                genero["porcentaje"] = calcular_porcentaje(genero["puntos"], dict_acumuladores[0]["cantidad_usuarios"])

            lista_estadisticas_generales[0]["promedio_edad"] = promediar(dict_acumuladores[0]["acumulador_edad"], dict_acumuladores[0]["cantidad_usuarios"])
            lista_estadisticas_generales[0]["porcentaje_usuarios_con_amigos"] = calcular_porcentaje(dict_acumuladores[0]["usuarios_con_amigos"], dict_acumuladores[0]["cantidad_usuarios"])

            mostrar_estadisticas_V2(lista_estadisticas_generales, lista_estadisticas_genero, dict_acumuladores, lista_juegos, lista_puntos_genero_juegos, lista_usuarios)
                                # aca si no gusta solo hay que descomentar las lineas comentadas, sacarle el V2 de esta funcion y sacarle el parametro lista de usuarios || falta cambiar lo de cancantidad recomendaciones
            #endregion 
        case 4:
            print("\nSaliendo...")
            break
