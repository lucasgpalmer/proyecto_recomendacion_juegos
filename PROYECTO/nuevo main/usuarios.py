from inputs import *
from menu import *

usuarios = [] # ver donde poner, ahora tmb esta en main
generos = ["masculino", "femenino", "no binario"] #ver donde meterlos
generos_juegos = ["Accion", "Aventura", "RPG", "Estrategia", "Simulacion", "Deportes", "Carreras", "Terror", "Puzzle", "Plataformas", "Sandbox", "Roguelike", "Supervivencia", "Lucha"]
modos_de_juego = ["Solo", "Cooperativo", "Competitivo"]


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

    mostrar_menu_genero_juegos(generos_juegos) # FALTA LOGICA PARA QUE SI ALCANZA EL TOTAL DE OPCIONES QUE BREAKEE AUTOMATICAMENTE. LO DEJO PENDIENTE
    usuario["generos_juego"] = []
    primera = True
    while True:
        ya_existe = False
        if primera:
            genero_juego = pedir_entero(f"Ingrese una opcion [1-{len(generos_juegos)}]: ", f"ERROR. Ingrese una opcion numérica [1-{len(generos_juegos)}]: ")
            while not validar_rango(genero_juego, 1, len(generos_juegos)):
                genero_juego = pedir_entero(f"ERROR. Ingrese una opcion valida [1-{len(generos_juegos)}]: ", f"ERROR. Ingrese una opcion numérica [1-{len(generos_juegos)}]: ")
            genero_juego = transformar_lower(generos_juegos[genero_juego - 1]) #conversion de num a str
            primera = False
        else:
            print("Generos seleccionados: ", end="")
            mostrar_lista(usuario["generos_juego"])
            genero_juego = pedir_entero(f"Ingrese otra opcion si desea [1-{len(generos_juegos)}] o [0] para finalizar: ", f"ERROR. Ingrese una opcion numérica [1-{len(generos_juegos)}] o [0]: ")
            while not validar_rango(genero_juego, 0, len(generos_juegos)):
                genero_juego = pedir_entero(f"ERROR. Ingrese una opcion valida [1-{len(generos_juegos)}] o [0]: ", f"ERROR. Ingrese una opcion numérica [1-{len(generos_juegos)}] o [0]: ")
            if genero_juego == 0:
                break
            genero_juego = transformar_lower(generos_juegos[genero_juego - 1])
            for genero in usuario["generos_juego"]:
                if genero == genero_juego:
                    print(f"{genero_juego} ya fue seleccionado!") #Se ve en minus el genero, maybe capitalize
                    ya_existe = True
                    break
        if not ya_existe:
            usuario["generos_juego"].append(genero_juego)

    usuario["modos_de_juego"] = [] # FALTA LOGICA PARA QUE SI ALCANZA EL TOTAL DE OPCIONES QUE BREAKEE AUTOMATICAMENTE. LO DEJO PENDIENTE
    primera = True
    while True:
        ya_existe = False
        if primera:
            modo_de_juego = pedir_cadena("Ingrese un modo de juego [Solo/Cooperativo/Competitivo]: ","ERROR. Ingrese un modo de juego valido [Solo/Cooperativo/Competitivo]: ", True)
            while not validar_coincidencia(modo_de_juego, modos_de_juego):
                modo_de_juego = pedir_cadena("ERROR. Ingrese un modo de juego valido [Solo/Cooperativo/Competitivo]: ","ERROR. Ingrese un modo de juego valido [Solo/Cooperativo/Competitivo]: ", True)
            primera = False
        else:
            print("Modos de juegos selecionados: ", end="")
            mostrar_lista(usuario["modos_de_juego"])
            modo_de_juego = pedir_cadena("Ingrese un modo de juego [Solo/Cooperativo/Competitivo] o [N] para finalizar: ","ERROR. Ingrese un modo de juego valido [Solo/Cooperativo/Competitivo] o [N]: ", True)
            while not validar_coincidencia(modo_de_juego, modos_de_juego) and modo_de_juego != "n":
                modo_de_juego = pedir_cadena("ERROR. Ingrese un modo de juego valido [Solo/Cooperativo/Competitivo] o [N]: ","ERROR. Ingrese un modo de juego valido [Solo/Cooperativo/Competitivo] o [N]: ", True)
            if modo_de_juego == "n":
                break
            for modo in usuario["modos_de_juego"]:
                if modo == modo_de_juego:
                    print(f"{modo_de_juego} ya fue seleccionado!")
                    ya_existe = True
                    break
        if not ya_existe:
            usuario["modos_de_juego"].append(modo_de_juego)

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

