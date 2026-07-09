from calculos_generales import *
from cadenas import *
from config import *
from listas import *
from mostrar_estadisticas import *


def mostrar_estadisticas_V2(lista_estadisticas_generales : list, lista_estadisticas_genero : list, dict_acumuladores : list, lista_juegos : list, lista_puntos_genero_juegos : list, lista_usuarios : list):

    print(f"El promedio de edad de todos los usuarios ingresados es de:" + b + f" {lista_estadisticas_generales[0]["promedio_edad"]:.1f} " + rs + "años")
    print(f"El usuario ingresado de mayor edad tiene" + b + f" {lista_estadisticas_generales[0]["edad_maxima"]} " + rs + "años.")
    print(f"El usuario ingresado de menor edad tiene" + b + f" {lista_estadisticas_generales[0]["edad_minima"]} " + rs + "años.\n")
    
    for genero in lista_estadisticas_genero:
        if genero["puntos"] > 0:
            print(f"Los usuarios {genero["genero"]} tienen un promedio de" + g + f" {genero["promedio"]:.1f}$ " + rs + "de presupuesto.")
            print("Representan el" + m + f" {genero["porcentaje"]:.1f}% " + rs + "de los usuarios totales.\n")
        else: 
            print(r + f"Ningún usuario es {genero["genero"]}  •︵• \n" + rs)

    if dict_acumuladores[0]["usuarios_con_amigos"] > 0:
        print("El" + m + f" {lista_estadisticas_generales[0]["porcentaje_usuarios_con_amigos"]:.1f}% " + rs + "de los usuarios totales juega con amigos ദ്ദി◝ ⩊ ◜.ᐟ\n")
    else:
        print(r + "Ningún usuario ingresado juega con amigos •︵• \n" + rs)

    if lista_estadisticas_generales[0]["hay_pc_alta"] == True:
        print("El usuario con pc de gama alta con mayor presupuesto tiene" + g + f" {dict_acumuladores[0]["max_presupuesto_pc_alta"]} " + rs + "USD disponible.\n")
    else:
        print(r + "No se encontraron usuarios con pc de gama alta.\n" + rs)

    print("Cantidad de veces que se recomendó cada juego:\n")

    frecuencias = calcular_frecuencias(lista_juegos, lista_usuarios)
    mostrar_frecuencia_recomendacion_V2(lista_juegos, frecuencias)  

    print("\nA continuación podrá ver un gráfico que indica cuantas veces se ingresó cada genero de juego:")
    print(r + "(A)cción" + a + " (H)istoria " + y + "(E)strategia" + rs)
    graficar_barras(lista_puntos_genero_juegos)

    print("""===============================================================================================================================""")

def calcular_frecuencias(lista_juegos, lista_usuarios): ### creada para frecuencia

    frecuencias = {}

    for juego in lista_juegos:
        frecuencias[juego["nombre"]] = 0

    for usuario in lista_usuarios:

        for recomendacion in usuario["Recomendaciones"]:

            if recomendacion in frecuencias:
                frecuencias[recomendacion] += 1

    return frecuencias

def mostrar_frecuencia_recomendacion_V2(lista_juegos : list, frecuencias) -> None: 
    '''
    ### ¿Qué hace?
    Muestra el contenido de dos listas.
    ### ¿Qué recibe?
    lista_a (list): Una de las lista que se desea mostrar.
    lista_b (list): La otra lista que se desea mostrar.
    ### ¿Qué retorna?
    None.
    '''
    for juego in lista_juegos:
        print(juego["nombre"] + " " * (35 - len(juego["nombre"])) + ": " + str(frecuencias[juego["nombre"]]))
