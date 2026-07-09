from calculos_generales import *
from config import *

def promediar(acumulador : int, cantidad : int) -> float:
    '''
    ### ¿Qué hace?
        Calcula un promedio.
    ### ¿Qué recibe?
        -acumulador (int): El total acumulado que se desea promediar.
        -cantidad (int): Cantidad total con la que se desea promediar.
    ### ¿Qué retorna?
        promedio (float): El promedio calculado.
    '''

    promedio = acumulador / cantidad
    return promedio

def calcular_porcentaje(condicion : int, cantidad : int) -> float:
    '''
    ### ¿Qué hace?
        Calcula un porcentaje.
    ### ¿Qué recibe?
        -Condicion (int) : La condición la cual se desea calcular el porcentaje.
        -Cantidad : La cantidad por la cual se va a dividir la condición.
    ### ¿Qué retorna?
        porcentaje (float) : Retorna el porcentaje calculado.
    '''
    
    porcentaje = (condicion * 100) / cantidad
    return porcentaje
