### Subclase ClientePremium (herencia) + polimorfismo.

from modulos.cliente import Cliente


class ClientePremium(Cliente):
    """
    ClientePremium: hereda de Cliente.
    Tiene un atributo específico: puntos.
    """

    def __init__(self, cliente_id: int, nombre: str, email: str, telefono: str, direccion: str, puntos: int = 0):
        super().__init__(cliente_id, nombre, email, telefono, direccion)
        self.puntos = puntos

    def mostrar_info(self) -> str:
        return super().mostrar_info() + f" | Tipo: Premium | Puntos: {self.puntos}"

    def beneficio_exclusivo(self) -> str:
        return "Beneficio Premium: soporte prioritario y puntos extra."
