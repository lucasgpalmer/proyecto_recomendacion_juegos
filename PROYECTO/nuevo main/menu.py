def mostrar_menu(opciones : list) -> None:
    print("\n=== MENÚ ==================\n")

    for i in range(len(opciones)):
        print(f"{i + 1}- {opciones[i]}")

    print()

def mostrar_menu_genero_juegos(opciones : list) -> None:
    print("Ingrese su genero de juego favorito:\n")

    for i in range(len(opciones)):
        print(f"{i + 1}- {opciones[i]}")

    print()


## VVV CHEKEARLA BIEN VVV
def mostrar_lista(lista: list) -> None:
    for i in range(len(lista)):
        if i == len(lista) - 1:
            print(lista[i].capitalize(), end="")
        else:
            print(lista[i].capitalize(), end=", ")
    print()
