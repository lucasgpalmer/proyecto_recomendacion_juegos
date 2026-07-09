from inputs import *
from menu import *

usuarios = [] # ver donde poner, ahora tmb esta en main
generos = ["masculino", "femenino", "no binario"] #ver donde meterlos
generos_juegos = ["Accion", "Aventura", "RPG", "Estrategia", "Simulacion", "Deportes", "Carreras", "Terror", "Puzzle", "Plataformas", "Sandbox", "Roguelike", "Supervivencia", "Lucha"]

def ingresar_usuario(usuarios : list):
    usuario = {}

    usuario["id"] = len(usuarios) + 1
    usuario["nombre_usuario"] = input("Ingrese su nombre de usuario: ") #Pensar en que validaciones si son necesarias.. como maximo de caracteres, espacios, etc..
    #   Aca la logica de si es usuario ya ingresado o no
    print(f"Bienvenid@ {usuario["nombre_usuario"]} al sistema de recomendación de videojuegos.")
    print("A continuación le pediremos que ingrese algunos datos.")

    usuario["edad"] = pedir_entero("Ingrese su edad: ", "ERROR. Ingrese una edad válida solo usando números (Minímo 8 años, máximo 100): ")
    while not validar_rango(usuario["edad"], 8, 100):
        usuario["edad"] = pedir_entero("ERROR. Ingrese una edad validad (Minímo 8 años, máximo 100): ", "ERROR. Ingrese una edad válida solo usando números (Minímo 8 años, máximo 100): ")

    usuario["genero"] = pedir_cadena("Ingrese su genero [Masculino / Femenino / No Binario]: ", "ERROR. Ingrese un genero valido [Masculino / Femenino / No Binario]: ", True)
    while not validar_coincidencia(usuario["genero"], generos):
        usuario["genero"] = pedir_cadena("ERROR. Ingrese un genero valido [Masculino / Femenino / No Binario]: " ,"ERROR. Ingrese un genero valido [Masculino / Femenino / No Binario]: ", True)

    mostrar_menu_genero_juegos(generos_juegos) # FALTA LOGICA PARA QUE PUEDA ELEGIR MAS DE 1 GENERO
    usuario["genero_juego"] = pedir_entero(f"Ingrese una opcion [1-{len(generos_juegos)}]: ", f"ERROR. Ingrese una opcion numérica [1-{len(generos_juegos)}]: ")
    while not validar_rango(usuario["genero_juego"], 1, len(generos_juegos)):
        usuario["genero_juego"] = pedir_entero(f"ERROR. Ingrese una opcion valida [1-{len(generos_juegos)}]: ", f"ERROR. Ingrese una opcion numérica [1-{len(generos_juegos)}]: ")
    usuario["genero_juego"] = transformar_lower(generos_juegos[usuario["genero_juego"] - 1])

    usuario["modo_de_juego"]
    usuario["nivel_de_compromiso"]
    usuario["duracion_preferida"]
    usuario["plataforma"]
    usuario["gama"]
    usuario["espacio_disco"]
    usuario["presupuesto"]

    usuarios.append(usuario)

def mostrar_usuario(usuario : dict):
    for key in usuario:
        print(f"{key}: {usuario[key]}")



def ver_usuarios():
    print("VER USUARIOS")

