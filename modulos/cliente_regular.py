##### Subclase ClienteRegular (herencia) + polimorfismo (redefinir mostrar_info).

from modulos.cliente import Cliente


class ClienteRegular(Cliente):
    """
    ClienteRegular: hereda de Cliente.
    Tiene un atributo específico: descuento (por ejemplo, 0 a 100).
    
    """

    def __init__(self, cliente_id: int, nombre: str, email: str, telefono: str, direccion: str, descuento: float = 0.0):
        super().__init__(cliente_id, nombre, email, telefono, direccion)
        self.descuento = descuento

    def mostrar_info(self) -> str:
        return super().mostrar_info() + f" | Tipo: Regular | Descuento: {self.descuento}%"

    def beneficio_exclusivo(self) -> str:
        return "Beneficio Regular: descuentos básicos."
