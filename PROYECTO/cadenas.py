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

def transformar_lista_a_cadena(lista: list) -> str:
    '''
    ### ¿Qué hace?
        Toma una lista y la pasa a cadena.
    ### ¿Qué recibe?
        lista (list): La lista a transformar.
    ### ¿Qué retorna?
        str: La lista transformada en cadena.
    '''
    cadena = ""
    
    for i in range(len(lista)):
        cadena += lista[i]

        if i != len(lista) - 1:
            cadena += ", "

    return cadena