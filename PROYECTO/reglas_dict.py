def sumar_puntos(lista : list, key : str, opcion_a_comparar : str | int | float,  condicion : str = "==", puntos : str = "puntos", cantidad_a_sumar : int | float = 1) -> None:
    '''
    ### ¿Qué hace?
        Recorre una lista de diccionarios comparando el valor de una clave determinada con un valor buscado.
        Si la condición se cumple, suma una cantidad determinada de puntos al juego correspondiente.

    ### ¿Qué recibe?
        - lista (list): Lista de diccionarios con los datos de los juegos.
        - clave_a_comparar (str): Clave del diccionario que se desea comparar.
        - opcion_a_comparar (str | int | float): Valor buscado.
        - condicion (str = "==" / "!=" / "<=" / ">=" / "<" / ">"): Condición a comparar.
        - cantidad_a_sumar (int | float = 1): Cantidad de puntos a sumar.

    ### ¿Qué retorna?
        None.
    '''
    for juego in lista:
        if condicion == "==" and juego[key] == opcion_a_comparar:
                juego[puntos] += cantidad_a_sumar
        elif condicion == "!=" and juego[key] != opcion_a_comparar:
                juego[puntos] += cantidad_a_sumar
        elif condicion == "<=" and juego[key] <= opcion_a_comparar:
                juego[puntos] += cantidad_a_sumar
        elif condicion == ">=" and juego[key] >= opcion_a_comparar:
                juego[puntos] += cantidad_a_sumar
        elif condicion == "<" and juego[key] < opcion_a_comparar:
                juego[puntos] += cantidad_a_sumar
        elif condicion == ">" and juego[key] > opcion_a_comparar:
                juego[puntos] += cantidad_a_sumar

def anular_puntos(lista : list, key : str, opcion_a_comparar : str | int | float, condicion : str = "==", puntos : str = "puntos") -> None:
    '''
    ### ¿Qué hace?
        Recorre una lista de diccionarios comparando el valor de una clave determinada con un valor buscado.
        Si la condición se cumple, establece en 0 el valor de la clave de puntaje del diccionario correspondiente.

    ### ¿Qué recibe?
        - lista (list): Lista de diccionarios con los datos de los juegos.
        - clave_a_comparar (str): Clave del diccionario que se desea comparar.
        - opcion_a_comparar (str | int | float): Valor buscado.
        - puntos (str = "puntos"): Clave del diccionario que contiene el puntaje a modificar.
        - condicion (str = "==" / "!=" / "<=" / ">=" / "<" / ">"): Condición a comparar.

    ### ¿Qué retorna?
        None.
    '''
    for juego in lista:
        if condicion == "==" and juego[key] == opcion_a_comparar:
                juego[puntos] = 0
        elif condicion == "!=" and juego[key] != opcion_a_comparar:
                juego[puntos] = 0
        elif condicion == "<=" and juego[key] <= opcion_a_comparar:
                juego[puntos] = 0
        elif condicion == ">=" and juego[key] >= opcion_a_comparar:
                juego[puntos] = 0
        elif condicion == "<" and juego[key] < opcion_a_comparar:
                juego[puntos] = 0
        elif condicion == ">" and juego[key] > opcion_a_comparar:
                juego[puntos] = 0