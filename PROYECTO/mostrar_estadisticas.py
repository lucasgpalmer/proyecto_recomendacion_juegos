from calculos_generales import *
from cadenas import *
from config import *
from listas import *


def mostrar_usuarios(lista_usuarios : list) -> None:
    for usuario in lista_usuarios:
        print(f"Id: {usuario["id_usuario"]}\t  || Nombre: {usuario["Nombre"]}\t  Edad: {usuario["Edad"]}\t  Juego Fav: {usuario["Juego favorito"]}")

def mostrar_usuario(usuario : int) -> None:
    print(f"""
Respuestas ingresadas por el usuario "{usuario["Nombre"]}":
- Id: {usuario["id_usuario"]}
- Nombre: {usuario["Nombre"]}
- Juego Fav: {usuario["Juego favorito"]}
- Edad: {usuario["Edad"]}
- Genero: {usuario["Genero"]}
- Genero juego: {usuario["Genero de juego"]}
- Modo de juego: {usuario["Modo de juego"]}
- Cantidad de amigos: {usuario["Cantidad de amigos"]}
- Perfil de jugador: {usuario["Perfil de jugador"]}
- Plataforma: {usuario["Plataforma"]}
- Gama: {usuario["Gama"]}
- Espacio disponible en disco: {usuario["Espacio en disco"]}
- Horas que juega al dia: {usuario["Horas"]}
- Presupuesto: {usuario["Presupuesto"]}
- Recomendaciones: {mostrar_lista(usuario["Recomendaciones"])}
""")

def mostrar_estadisticas(lista_estadisticas_generales : list, lista_estadisticas_genero : list, dict_acumuladores : list, lista_juegos : list, lista_puntos_genero_juegos : list):

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

    mostrar_frecuencia_recomendacion(lista_juegos)

    print("\nA continuación podrá ver un gráfico que indica cuantas veces se ingresó cada genero de juego:")
    print(r + "(A)cción" + a + " (H)istoria " + y + "(E)strategia" + rs)
    graficar_barras(lista_puntos_genero_juegos)

    print("""===============================================================================================================================""")

def mostrar_frecuencia_recomendacion(lista_juegos : list) -> None: 
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
        print(juego["nombre"] + " " * (35 - len(juego["nombre"])) + ": " + str(juego["frecuencia_recomendacion"]))

def graficar_barras(lista : list) -> None:
    '''
    ### ¿Qué hace?
        Muestra un gráfico de barras.
    ### ¿Qué recibe?
        -lista (list): La lista que se desea graficar.
    ### ¿Qué retorna?
        None.
    '''

    altura_max = lista[0]["puntos"]
    altura_max = encontrar_maximo(lista[1]["puntos"], altura_max)
    altura_max = encontrar_maximo(lista[2]["puntos"], altura_max)

    for i in range(altura_max, 0, -1):
        fila = ""

        if lista[0]["puntos"] >= i:
            fila += r + "    █  " + rs
        else:
            fila += "       "

        if lista[1]["puntos"] >= i:
            fila += a + "       █  " + rs
        else:
            fila += "          "

        if lista[2]["puntos"] >= i:
            fila += y + "          █  " + rs
        else:
            fila += "             "

        print(fila)

def mostrar_datos(nombre : str, juego_favorito : str, recomendacion : list, cantidad_recomendaciones : int) -> None:
        '''
        ### ¿Qué hace?
            Muestra los datos de salida.
        ### ¿Qué recibe?
            - nombre (str): Nombre ingresado por el usuario.
            - juego_favorito (str): Juego favorito ingresado por el usuario.
            - recomendacion (list): Lista de recomendaciones de juegos.
            - cantidad_recomendaciones (int): Cantidad de juegos a recomendar.
        ### ¿Qué retorna?
            None.
        '''
        print("""= RECOMENDACIONES =============================================================================================================\n""")
        print("Hola de nuevo, " + m + f"{nombre}" + rs)
        print("Buen juego el " + m + f"{juego_favorito}" + rs) 
        print("En base a sus respuestas creemos que...")
        
        recomendaciones = transformar_lista_a_cadena(recomendacion)
        if recomendacion == []:
            print(r + "No hay ningún juego compatible con lo que contestó •︵•" + rs)
        else:
            if cantidad_recomendaciones == 1:
                print("El juego " + g + f"{recomendaciones}" + rs + " es apropiado para usted " + y + "☺︎" + rs)
            else:
                print("Los juegos " + g + f"{recomendaciones}" + rs + " son apropiados para usted " + y + "☺︎" + rs)

        print("Vuelva pronto ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧")



        print("""\n===============================================================================================================================""")