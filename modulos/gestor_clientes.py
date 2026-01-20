#### Clase GestorClientes: almacena múltiples clientes y hace CRUD básico.

from modulos.excepciones import ClienteExistenteError, ClienteNoEncontradoError


class GestorClientes:
    """
    Administra una lista de clientes (pueden ser de distintas subclases).
    """

    def __init__(self):
        self.clientes = []  # lista de objetos Cliente/ClienteRegular/ClientePremium/ClienteCorporativo

    def agregar_cliente(self, cliente):
        """
        Agrega un cliente si no existe otro con el mismo email o el mismo ID.
        """
        for c in self.clientes:
            if c.id == cliente.id:
                raise ClienteExistenteError("Ya existe un cliente con ese ID.")
            if c.email.lower() == cliente.email.lower():
                raise ClienteExistenteError("Ya existe un cliente con ese email.")
        self.clientes.append(cliente)

    def listar_clientes(self) -> list:
        """
        Devuelve la lista completa.
        """
        return self.clientes

    def buscar_por_id(self, cliente_id: int):
        """
        Busca cliente por ID.
        """
        for c in self.clientes:
            if c.id == cliente_id:
                return c
        raise ClienteNoEncontradoError("ERROR! Cliente no encontrado por ID.")

    def buscar_por_email(self, email: str):
        """
        Busca cliente por email.
        """
        for c in self.clientes:
            if c.email.lower() == email.lower():
                return c
        raise ClienteNoEncontradoError("ERROR! Cliente no encontrado por email.")

    def actualizar_cliente(
        self,
        cliente_id: int,
        nuevo_nombre: str,
        nuevo_email: str,
        nuevo_telefono: str,
        nueva_direccion: str
    ):
        """
        Actualiza datos base del cliente.
        Nota: el email se valida desde el setter del cliente.
        """
        cliente = self.buscar_por_id(cliente_id)

        # Si cambia el email, verificamos que no se repita
        if cliente.email.lower() != nuevo_email.lower():
            for c in self.clientes:
                if c.email.lower() == nuevo_email.lower():
                    raise ClienteExistenteError(
                        "ERROR! No se puede actualizar: ese email ya existe en otro cliente."
                    )

        cliente.nombre = nuevo_nombre
        cliente.email = nuevo_email
        cliente.telefono = nuevo_telefono
        cliente.direccion = nueva_direccion

        return cliente

    def eliminar_cliente(self, cliente_id: int):
        """
        Eliminar a un cliente por su ID.
        """
        cliente = self.buscar_por_id(cliente_id)
        self.clientes.remove(cliente)
        return cliente
