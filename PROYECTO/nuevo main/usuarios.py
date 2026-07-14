from inputs import *
from menu import *

usuarios = [] # ver donde poner, ahora tmb esta en main
generos = ["Masculino", "Femenino", "No Binario"] #ver donde meterlos
generos_juegos = ["Accion", "Aventura", "RPG", "Estrategia", "Simulacion", "Deportes", "Carreras", "Terror", "Puzzle", "Plataformas", "Sandbox", "Roguelike", "Supervivencia", "Lucha"]
modos_de_juego = ["Solo", "Cooperativo", "Competitivo"]
niveles_compromiso = ["Casual", "Dedicado", "Competitivo"]
duraciones_preferidas = ["Corto", "Medio", "Largo"]
plataformas = ["PC", "PlayStation", "Xbox", "Switch"]
gamas = ["Baja", "Media", "Alta"]

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

    usuario["genero"] = pedir_cadena("Ingrese su genero [Masculino/Femenino/No Binario]: ", "ERROR. Ingrese un genero valido [Masculino/Femenino/No Binario]: ", True)
    while not validar_coincidencia(usuario["genero"], generos):
        usuario["genero"] = pedir_cadena("ERROR. Ingrese un genero valido [Masculino/Femenino/No Binario]: " ,"ERROR. Ingrese un genero valido [Masculino/Femenino/No Binario]: ", True)

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

    usuario["niveles_compromiso"] = [] # FALTA LOGICA PARA QUE SI ALCANZA EL TOTAL DE OPCIONES QUE BREAKEE AUTOMATICAMENTE. LO DEJO PENDIENTE
    primera = True
    while True:
        ya_existe = False
        if primera:
            nivel_compromiso = pedir_cadena(
                "Ingrese un nivel de compromiso [Casual/Dedicado/Competitivo]: ",
                "ERROR. Ingrese un nivel de compromiso valido [Casual/Dedicado/Competitivo]: ",
                True
            )
            while not validar_coincidencia(nivel_compromiso, niveles_compromiso):
                nivel_compromiso = pedir_cadena(
                    "ERROR. Ingrese un nivel de compromiso valido [Casual/Dedicado/Competitivo]: ",
                    "ERROR. Ingrese un nivel de compromiso valido [Casual/Dedicado/Competitivo]: ",
                    True
                )
            primera = False
        else:
            print("Niveles de compromiso seleccionados: ", end="")
            mostrar_lista(usuario["niveles_compromiso"])

            nivel_compromiso = pedir_cadena(
                "Ingrese otro nivel de compromiso [Casual/Dedicado/Competitivo] o [N] para finalizar: ",
                "ERROR. Ingrese un nivel de compromiso valido [Casual/Dedicado/Competitivo] o [N]: ",
                True
            )
            while not validar_coincidencia(nivel_compromiso, niveles_compromiso) and nivel_compromiso != "n":
                nivel_compromiso = pedir_cadena(
                    "ERROR. Ingrese un nivel de compromiso valido [Casual/Dedicado/Competitivo] o [N]: ",
                    "ERROR. Ingrese un nivel de compromiso valido [Casual/Dedicado/Competitivo] o [N]: ",
                    True
                )

            if nivel_compromiso == "n":
                break

            for nivel in usuario["niveles_compromiso"]:
                if nivel == nivel_compromiso:
                    print(f"{nivel_compromiso} ya fue seleccionado!")
                    ya_existe = True
                    break

        if not ya_existe:
            usuario["niveles_compromiso"].append(nivel_compromiso)


    usuario["duraciones_preferidas"] = [] # FALTA LOGICA PARA QUE SI ALCANZA EL TOTAL DE OPCIONES QUE BREAKEE AUTOMATICAMENTE. LO DEJO PENDIENTE
    primera = True
    while True:
        ya_existe = False
        if primera:
            duracion_preferida = pedir_cadena(
                "Ingrese una duración preferida [Corto/Medio/Largo]: ",
                "ERROR. Ingrese una duración preferida valida [Corto/Medio/Largo]: ",
                True
            )
            while not validar_coincidencia(duracion_preferida, duraciones_preferidas):
                duracion_preferida = pedir_cadena(
                    "ERROR. Ingrese una duración preferida valida [Corto/Medio/Largo]: ",
                    "ERROR. Ingrese una duración preferida valida [Corto/Medio/Largo]: ",
                    True
                )
            primera = False
        else:
            print("Duraciones preferidas seleccionadas: ", end="")
            mostrar_lista(usuario["duraciones_preferidas"])

            duracion_preferida = pedir_cadena(
                "Ingrese otra duración preferida [Corto/Medio/Largo] o [N] para finalizar: ",
                "ERROR. Ingrese una duración preferida valida [Corto/Medio/Largo] o [N]: ",
                True
            )

            while not validar_coincidencia(duracion_preferida, duraciones_preferidas) and duracion_preferida != "n":
                duracion_preferida = pedir_cadena(
                    "ERROR. Ingrese una duración preferida valida [Corto/Medio/Largo] o [N]: ",
                    "ERROR. Ingrese una duración preferida valida [Corto/Medio/Largo] o [N]: ",
                    True
                )

            if duracion_preferida == "n":
                break

            for duracion in usuario["duraciones_preferidas"]:
                if duracion == duracion_preferida:
                    print(f"{duracion_preferida} ya fue seleccionado!")
                    ya_existe = True
                    break

        if not ya_existe:
            usuario["duraciones_preferidas"].append(duracion_preferida)

    usuario["plataformas"] = [] # FALTA LOGICA PARA QUE SI ALCANZA EL TOTAL DE OPCIONES QUE BREAKEE AUTOMATICAMENTE. LO DEJO PENDIENTE
    primera = True
    while True:
        ya_existe = False
        if primera:
            plataforma = pedir_cadena(
                "Ingrese una plataforma [PC/PlayStation/Xbox/Switch]: ",
                "ERROR. Ingrese una plataforma valida [PC/PlayStation/Xbox/Switch]: ",
                True
            )
            while not validar_coincidencia(plataforma, plataformas):
                plataforma = pedir_cadena(
                    "ERROR. Ingrese una plataforma valida [PC/PlayStation/Xbox/Switch]: ",
                    "ERROR. Ingrese una plataforma valida [PC/PlayStation/Xbox/Switch]: ",
                    True
                )
            primera = False
        else:
            print("Plataformas seleccionadas: ", end="")
            mostrar_lista(usuario["plataformas"])

            plataforma = pedir_cadena(
                "Ingrese otra plataforma [PC/PlayStation/Xbox/Switch] o [N] para finalizar: ",
                "ERROR. Ingrese una plataforma valida [PC/PlayStation/Xbox/Switch] o [N]: ",
                True
            )

            while not validar_coincidencia(plataforma, plataformas) and plataforma != "n":
                plataforma = pedir_cadena(
                    "ERROR. Ingrese una plataforma valida [PC/PlayStation/Xbox/Switch] o [N]: ",
                    "ERROR. Ingrese una plataforma valida [PC/PlayStation/Xbox/Switch] o [N]: ",
                    True
                )

            if plataforma == "n":
                break

            for plataforma_seleccionada in usuario["plataformas"]:
                if plataforma_seleccionada == plataforma:
                    print(f"{plataforma} ya fue seleccionada!")
                    ya_existe = True
                    break

        if not ya_existe:
            usuario["plataformas"].append(plataforma)

    usuario["gama"] = "-"
    for plataforma in usuario["plataformas"]:
        if plataforma == "pc":
            usuario["gama"] = pedir_cadena(
                "Ingrese la gama de su PC [Baja / Media / Alta]: ",
                "ERROR. Ingrese una gama valida [Baja / Media / Alta]: ",
                True
            )
            while not validar_coincidencia(usuario["gama"], gamas):
                usuario["gama"] = pedir_cadena(
                    "ERROR. Ingrese una gama valida [Baja / Media / Alta]: ",
                    "ERROR. Ingrese una gama valida [Baja / Media / Alta]: ",
                    True
                )
            break

    usuario["espacio_disco"] = pedir_entero(
        "Ingrese su espacio en disco disponible (GB): ",
        "ERROR. Ingrese solo un valor numerico: "
    )
    while usuario["espacio_disco"] < 1:
        usuario["espacio_disco"] = pedir_entero(
            "ERROR. Ingrese un espacio mayor a 0 GB: ",
            "ERROR. Ingrese solo un valor numerico: "
        )

    usuario["presupuesto"] = pedir_entero(
        "Ingrese su presupuesto disponible (USD): ",
        "ERROR. Ingrese un valor numerico no negativo: "
    )

    usuarios.append(usuario)
    # retornar usuario? desp veo beneficios

def mostrar_usuario(usuario : dict):
    for key in usuario:
        if type(usuario[key]) == list:
            print(f"{key}: ", end="")
            mostrar_lista(usuario[key])
        else:   
            print(f"{key}: {usuario[key]}")



def ver_usuarios():
    print("VER USUARIOS")

