def pedir_entero(mensaje : str = "Ingrese un entero: ", mensaje_error : str = "ERROR. Ingrese un entero: ") -> int:
    '''
    ### ¿Qué hace?
        Pide ingresar un entero y valida el type.
    ### ¿Qué recibe?
        - mensaje (str = "Ingrese un entero: "): Mensaje que se mostrara para pedir el entero.
        - mensaje_error (str = "ERROR. Ingrese un entero: "): Mensaje que se mostrara en caso de error.
    ### ¿Qué retorna?
        int: El entero que fue ingresado y validado.
    '''

    while True:
        numero = input(mensaje)

        if validar_entero(numero):
            return int(numero)

        mensaje = mensaje_error

def validar_entero(cadena: str) -> bool:
    '''
    ### ¿Qué hace?
        Valida si la cadena representa un número entero positivo.
    ### ¿Qué recibe?
        - cadena (str): Cadena a comparar.
    ### ¿Qué retorna?
        bool: True -> Si la cadena contiene solo números. | False -> Si la cadena contiene al menos un caracter diferente a un número.
    '''
    if cadena != "":
        validado = True
        for caracter in cadena:
            validado_actual = False
            for caracter_valido in "0123456789":
                if caracter == caracter_valido:
                    validado_actual = True
                    break
            if not validado_actual:
                validado = False
                break
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

def validar_coincidencia(opcion_ingresada : str, opciones : list) -> bool:
    opcion_ingresada = transformar_lower(opcion_ingresada)

    for opcion in opciones:
        if opcion_ingresada == transformar_lower(opcion):
            return True

    return False




#################################### vvvv chekear vvvv


def pedir_cadena(mensaje : str = "Ingrese una cadena: ", mensaje_error : str = "ERROR. Ingrese una cadena valida", lower : bool = False) -> str:
    '''
    ### ¿Qué hace?
        Pide una cadena y valida el type con opcion de transformarla a minusculas.
    ### ¿Qué recibe?
        - mensaje (str = "Ingrese una cadena: ): Mensaje que se mostrara para pedir la cadena.
        - mensaje_error (str = "ERROR. Ingrese una cadena valida"): Mensaje que se mostrara en caso de error.
        - lower (bool = False): Si se desea pasar o no la cadena a minusculas. 
    ### ¿Qué retorna?
        str: La cadena que fue ingresada y validada con opcion de transformala a minusculas.
    '''
    flag = True
    while True:
        if flag:
            cadena = input(mensaje)
            flag = False
        else:
            cadena = input(mensaje_error)
        if validar_str_type(cadena):
            cadena = eliminar_espacios_repetidos(cadena)
            if lower:
                return transformar_lower(cadena)
            else:
                return cadena

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

def eliminar_espacios_repetidos(texto: str) -> str:
    resultado = ""

    for caracter in texto:
        if caracter != " ":
            resultado += caracter
        else:
            if len(resultado) == 0 or resultado[-1] != " ":
                resultado += caracter

    return resultado

def transformar_lower(cadena: str) -> str:
    '''
    ### ¿Qué hace?
        Toma la cadena ingresada y transforma todas sus letras en minúsculas.
    ### ¿Qué recibe?
        cadena (str): La cadena a transformar
    ### ¿Qué retorna?
        str: La cadena ingresada en minúsculas.
    '''
    cadena_final = ""

    for caracter in cadena:
        indice_caracter = ord(caracter)

        if indice_caracter >= 65 and indice_caracter <= 90:
            indice_caracter += 32

        nuevo_caracter = chr(indice_caracter)
        cadena_final += nuevo_caracter

    return cadena_final