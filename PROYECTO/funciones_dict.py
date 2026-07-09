def agregar_usuario(lista : list, id_usuario : int, nombre : str, edad : int, genero : str, juego_favorito : str,
genero_juego : str, modo_de_juego : str, cantidad_de_amigos : int, perfil_de_jugador : str, plataforma : str, gama : str,
espacio_disco : int, horas : int, presupuesto : int, recomendacion : list) -> None:
    
    lista.append({
        "id_usuario" : id_usuario,
        "Nombre" : nombre,
        "Edad" : edad,
        "Genero" : genero,
        "Juego favorito" : juego_favorito,
        "Genero de juego" : genero_juego,
        "Modo de juego" : modo_de_juego,
        "Cantidad de amigos" : cantidad_de_amigos,
        "Perfil de jugador" : perfil_de_jugador,
        "Plataforma" : plataforma,
        "Gama" : gama,
        "Espacio en disco" : espacio_disco,
        "Horas" : horas,
        "Presupuesto" : presupuesto,
        "Recomendaciones" : recomendacion
    })

def modificar_usuario(lista: list, indice: int, id_usuario : int, nombre: str, edad: int, genero: str,juego_favorito: str,
genero_juego: str, modo_de_juego: str,cantidad_de_amigos: int, perfil_de_jugador: str, plataforma: str, gama: str,
espacio_disco: int, horas: int, presupuesto: int,recomendacion: list) -> None:

    lista[indice] = {
        "id_usuario" : id_usuario,
        "Nombre": nombre,
        "Edad": edad,
        "Genero": genero,
        "Juego favorito": juego_favorito,
        "Genero de juego": genero_juego,
        "Modo de juego": modo_de_juego,
        "Cantidad de amigos": cantidad_de_amigos,
        "Perfil de jugador": perfil_de_jugador,
        "Plataforma": plataforma,
        "Gama": gama,
        "Espacio en disco": espacio_disco,
        "Horas": horas,
        "Presupuesto": presupuesto,
        "Recomendaciones": recomendacion
    }

def buscar_usuario(lista: list, nombre: str) -> int:
    for i in range(len(lista)):
        if lista[i]["Nombre"] == nombre:
            return i
    return -1

def sumar_puntos_si_son_iguales(lista_1 : list, lista_2 : list, clave_a_comparar : str, clave_a_comparar_2 : str, clave_a_sumar : str, cant_a_sumar : int|float = 1) -> None:

    establecer_puntos_lista_dict(lista_1, clave_a_sumar)  #paradigma???
    for i in lista_1:
        for j in lista_2:
            if i[clave_a_comparar] == j[clave_a_comparar_2] :
                i[clave_a_sumar] += cant_a_sumar

def establecer_puntos_lista_dict(lista_1 : list,  clave : str, valor : int | bool = 0) -> None:

    for i in lista_1:
        i[clave] = valor
