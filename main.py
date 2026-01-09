
from modulos.gestor_clientes import Cliente
from modulos.gestor_clientes import GestorClientes


def main() -> None:
    """
    Punto de entrada del programa.
    En Lección 1 solo creamos instancias y probamos impresión por consola.
    """

    # Creamos el gestor
    gestor = GestorClientes()



    # Creamos clientes
    cliente_1 = Cliente(
        cliente_id=1,
        nombre="Juan Pérez",
        email="juan.perez@gmail.com",
        telefono="+56 9 1111 2222",
        direccion="Av. Siempre Viva 123, Santiago"
    )

    cliente_2 = Cliente(
        cliente_id=2,
        nombre="María González",
        email="maria.gonzalez@gmail.com",
        telefono="+56 9 3333 4444",
        direccion="Calle Falsa 456, Valparaíso"
    )

    # agregamos clientes al gestor
    gestor.agregar_cliente(cliente_1)
    gestor.agregar_cliente(cliente_2)

    # Mostramos por consola usando __str__ (que llama a mostrar_info)
    print("=== CLIENTES REGISTRADOS ===\n")
    for cliente in gestor.listar_clientes():
        print(cliente)
        print("-" * 30)


if __name__ == "__main__":
    main()
