def mostrar_lista(lista_a : list, lista_b : list | None = None) -> None: 
    '''
    ### ¿Qué hace?
    Muestra el contenido de dos listas.
    ### ¿Qué recibe?
    lista_a (list): Una de las lista que se desea mostrar.
    lista_b (list): La otra lista que se desea mostrar.
    ### ¿Qué retorna?
    None.
    '''
    if lista_b == None:
        for i in range(len(lista_a)):
            print(f"{i+1}. {lista_a[i]}")
    else:
        for i in range(len(lista_a)):
            if verificar_longitud_listas(lista_a, lista_b):
                print(f"{i+1}. {lista_a[i]}: {lista_b[i]}")
            else:
                print("Se deben ingresar dos listas con longitudes iguales")

def verificar_longitud_listas(lista_a : list, lista_b : list) -> bool:
    '''
    ### ¿Qué hace?
    Verifica si la longitud de dos listas son iguales.
    ### ¿Qué recibe?
    lista_a (list): Una de las lista que se desea verificar.
    lista_b (list): La otra lista que se desea verificar.
    ### ¿Qué retorna?
    bool: True -> Si la longitud de las listas son iguales. | False -> Si la longitud de las listas son diferentes.
    '''
    if len(lista_a) == len(lista_b):
        return True
    else:
        return False
