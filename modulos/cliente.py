
class GestorClientes:
    def __init__(self):
        self.__clientes = []

    def agregar_cliente(self, cliente: Cliente):
        self.__clientes.append(cliente)

    def listar_clientes(self):
        return self.__clientes

class Cliente:
    """
    Define un cliente con sus atributos básicos.
    """
    def __init__(self, cliente_id: int, nombre: str, email: str, telefono: str, direccion: str) -> None:
        # Atributos privados (encapsulación básica)
        self.__cliente_id = cliente_id
        self.__nombre = nombre
        self.__email = email
        self.__telefono = telefono
        self.__direccion = direccion

    def mostrar_info(self) -> str:
        """
        Devuelve un texto con la información completa del cliente.
        En lecciones posteriores esta idea se reutiliza para polimorfismo.
        """
        return (
            f"ID: {self.__cliente_id}\n"
            f"Nombre: {self.__nombre}\n"
            f"Email: {self.__email}\n"
            f"Teléfono: {self.__telefono}\n"
            f"Dirección: {self.__direccion}"
        )

    def __str__(self) -> str:
        """
        Representación amigable del cliente al imprimirlo.
        Para Lección 1, lo más simple es devolver mostrar_info().
        """
        return self.mostrar_info()
