from validaciones_ant import *
from cadenas import *

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
    numero = input(mensaje)

    if validar_int_type(numero):
        return int(numero)

    return pedir_entero(mensaje_error, mensaje_error)

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

def pedir_flotante(mensaje : str = "Ingrese un flotante: ", mensaje_error : str = "ERROR. Ingrese un flotante: ") -> float:
    '''
    ### ¿Qué hace?
        Pide ingresar un flotante y valida el type.
    ### ¿Qué recibe?
        - mensaje (str = "Ingrese un flotante: "): Mensaje que se mostrara para pedir el entero.
        - mensaje_error (str = "ERROR. Ingrese un flotante: "): Mensaje que se mostrara en caso de error.
    ### ¿Qué retorna?
        float: El flotante que fue ingresado y validado.
    '''
    flag = True
    while True:
        if flag:
            numero = input(mensaje)
            flag = False
        else:
            numero = input(mensaje_error)
        if validar_float_type(numero):
            return float(numero)
