def encontrar_minimo(valor_ingresado : int | float , minimo : int | float) -> int:
    '''
    ### ¿Qué hace?
        Determina si el valor minimo es el valor ingresado o el minimo establecido.
    ### ¿Qué recibe?
        - valor_ingresado (int | float): Valor a comparar con el minimo.
        - minimo (int | float): Valor minimo
    ### ¿Qué retorna?
        int: El valor minimo entre el valor ingresado y el valor establecido.
    '''
    if valor_ingresado < minimo:
        minimo = valor_ingresado
    return minimo

def encontrar_maximo(valor_ingresado : int | float, maximo : int | float) -> int:
    '''
    ### ¿Qué hace?
        Determina si el valor maximo es el valor ingresado o el maximo establecido.
    ### ¿Qué recibe?
        - valor_ingresado (int | float): Valor a comparar con el maximo.
        - minimo (int | float): Valor maximo.
    ### ¿Qué retorna?
        int: El valor maximo entre el valor ingresado y el valor establecido.
    '''
    if valor_ingresado > maximo:
        maximo = valor_ingresado
    return maximo
