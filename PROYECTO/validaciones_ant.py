def validar_int_type(cadena: str) -> bool:
    '''
    ### ¿Qué hace?
        Valida si la cadena ingresada contiene un número.
    ### ¿Qué recibe?
        - cadena (str): Cadena a comparar.
    ### ¿Qué retorna?
        bool: True -> Si la cadena contiene solo números. | False -> Si la cadena contiene al menos un caracter diferente a un número.
    '''
    if type(cadena) == str and cadena != "":
        validado = True
        for caracter in cadena:
            validado_actual = False
            for caracter_valido in "0123456789":              #VALIDAMOS NEGATIVOS?
                if caracter == caracter_valido:
                    validado_actual = True
                    break
            if not validado_actual:
                validado = False
                break
    else:
        validado = False
    return validado

def validar_cadena(opcion_ingresada : str, opcion1 : str = None, opcion2 : str = None, opcion3 : str = None) -> bool:
    '''
    ### ¿Qué hace?
        Valida si la opcion ingresada es igual a una de las opciones predeterminadas.
    ### ¿Qué recibe?
        - opcion_ingresada (str): Opcion ingresada
        - opcion1 (str = None): Opcion predeterminada 1
        - opcion2 (str = None): Opcion predeterminada 2
        - opcion3 (str = None): Opcion predeterminada 3
    ### ¿Qué retorna?
        bool: True -> Si la opcion ingresada es igual a una predeterminada | False -> Si la opcion ingresada no es igual a ninguna predeterminada.
    '''
    if opcion_ingresada != opcion1 and opcion_ingresada != opcion2 and opcion_ingresada != opcion3:
        return False
    else:
        return True

def validar_str_type(cadena : str) -> bool: #No admite tildes, tildes = False
    '''
    ### ¿Qué hace?
        Valida si la cadena ingresada contiene números.
    ### ¿Qué recibe?
        - cadena (str): Cadena a validar.
    ### ¿Qué retorna?
        bool: True -> Si la cadena contiene solamente letras. | False -> Si la cadena contiene un caracter diferente a una letra.
    '''
    validado = True
    for caracter in cadena:
        ascii = ord(caracter)
        if not (ascii >= 65 and ascii <= 90) and not (ascii >= 97 and ascii <= 122) and not ascii == 32 and not ascii == 241 and not ascii == 209:
            validado = False
            break
    
    return validado

def validar_float_type(cadena: str) -> bool:
    '''
    ### ¿Qué hace?
        Valida si la cadena ingresada contiene un número y cuantos puntos tiene.
    ### ¿Qué recibe?
        - cadena (str): Cadena a comparar.
    ### ¿Qué retorna?
        bool: True -> Si la cadena contiene solo números y no más de un punto. | False -> Si la cadena contiene al menos un caracter diferente a un número y/o mas de un punto.
    '''
    if type(cadena) == str and cadena != "":
        validado = True
        cantidad_puntos = 0
        for caracter in cadena:
            validado_actual = False
            if caracter == ".":
                cantidad_puntos += 1
            for caracter_valido in "0123456789.":
                if caracter == caracter_valido:
                    validado_actual = True
                    break
            if not validado_actual:
                validado = False
                break
        if cantidad_puntos > 1:
            return False
    else:
        validado = False
    return validado

def validar_rango(numero : int | float, minimo : int | float = None, maximo : int | float = None) -> bool:
    '''
    ### ¿Qué hace?
        Valida si el número ingresado está dentro del rango requerido.
    ### ¿Qué recibe?
        - numero (int | float): El número a validar dentro del rango.
        - minimo (int | float): Determinado el mínimo posible dentro del rango.
        - maxima (int | float): Determinado el máximo posible dentro del rango.
    ### ¿Qué retorna?
        bool: True -> Si el número pertenece al rango. | False -> Si el número no pertenece al rango.
    '''
    return (minimo == None or numero >= minimo) and (maximo == None or numero <= maximo)

def eliminar_espacios_repetidos(texto: str) -> str:
    resultado = ""

    for caracter in texto:
        if caracter != " ":
            resultado += caracter
        else:
            if len(resultado) == 0 or resultado[-1] != " ":
                resultado += caracter

    return resultado