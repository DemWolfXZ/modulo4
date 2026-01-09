from modulos.cliente import Cliente


class GestorClientes:
    """
    Administra una colección de clientes.
    """

    def __init__(self) -> None:
        # Lista interna (privada por convención) donde se almacenan los clientes
        self.__clientes: list[Cliente] = []

    def agregar_cliente(self, cliente: Cliente) -> None:
        """
        Agrega un cliente a la lista interna.
        """
        self.__clientes.append(cliente)

    def listar_clientes(self) -> list[Cliente]:
        """
        Devuelve la lista de clientes para poder recorrerla desde main.
        """
        return self.__clientes
