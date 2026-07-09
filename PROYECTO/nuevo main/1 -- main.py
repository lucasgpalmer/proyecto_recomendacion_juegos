from inputs import *
from menu import *
from usuarios import *
from estadisticas import *
#from _ import *

def main():
    lista_opciones = [
        "INGRESAR USUARIO NUEVO",
        "VER USUARIOS",
        "VER ESTADISTICAS",
        "Salir"
    ]

    while True:
        #region menu
        mostrar_menu(lista_opciones)

        # VVV Ver como poner mas prolijo esto VVV
        opcion = pedir_entero(f"Ingrese una opción [1-{len(lista_opciones)}]: ", f"ERROR. Ingrese una opción numérica [1-{len(lista_opciones)}]: ")
        while not validar_rango(opcion, 1, len(lista_opciones)):
            opcion = pedir_entero(f"ERROR. Ingrese una opción valida [1-{len(lista_opciones)}]: ", f"ERROR. Ingrese una opción numérica [1-{len(lista_opciones)}]: ")
        #endregion
        #region utiles
        usuarios = [] #esto se repite en usuarios, ver bien donde lo dejamos
        #endregion

        match opcion:
            case 1:
                ingresar_usuario(usuarios)
                mostrar_usuario(usuarios[0])
            case 2:
                ver_usuarios()

            case 3:
                ver_estadisticas()

            case 4:
                print("Saliendo...")
                break


if __name__ == "__main__":
    main()