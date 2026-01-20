from modulos.cliente import Cliente




class ClienteCorporativo(Cliente):
    """
    ClienteCorporativo: hereda de Cliente.
    Tiene un atributo específico: empresa.
    """

    def __init__(self, cliente_id: int, nombre: str, email: str, telefono: str, direccion: str, empresa: str = "Sin empresa"):
        super().__init__(cliente_id, nombre, email, telefono, direccion)
        self.empresa = empresa.strip()

    def mostrar_info(self) -> str:
        return super().mostrar_info() + f" | Tipo: Corporativo | Empresa: {self.empresa}"

    def beneficio_exclusivo(self) -> str:
        return "Beneficio Corporativo: convenios y atención dedicada."
