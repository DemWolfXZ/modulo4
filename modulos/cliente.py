#### Clase base Cliente. Usa encapsulación (atributos privados + getters/setters).

from modulos.validaciones import validar_email, validar_telefono, validar_direccion


class Cliente:
    """
    Clase base Cliente.
    Atributos principales: id, nombre, email, telefono, direccion
    """

    def __init__(self, cliente_id: int, nombre: str, email: str, telefono: str, direccion: str):
        self.__id = cliente_id
        self.__nombre = nombre.strip()

        # Usamos setters para asegurar validación desde el inicio
        self.email = email
        self.telefono = telefono
        self.direccion = direccion

    # Getter de ID (solo lectura)
    @property
    def id(self) -> int:
        return self.__id

    # Getter/Setter nombre
    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, value: str):
        self.__nombre = value.strip()

    # Getter/Setter email con validación
    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, value: str):
        validar_email(value)
        self.__email = value.strip()

    # Getter/Setter telefono con validación
    @property
    def telefono(self) -> str:
        return self.__telefono

    @telefono.setter
    def telefono(self, value: str):
        validar_telefono(value)
        self.__telefono = value.strip()

    # Getter/Setter direccion con validación
    @property
    def direccion(self) -> str:
        return self.__direccion

    @direccion.setter
    def direccion(self, value: str):
        validar_direccion(value)
        self.__direccion = value.strip()

    def mostrar_info(self) -> str:
        """
        Método pensado para ser redefinido en subclases (polimorfismo).
        """
        return f"ID: {self.id} | Nombre: {self.nombre} | Email: {self.email} | Tel: {self.telefono} | Dir: {self.direccion}"

    def __str__(self) -> str:
        # Facilita la visualización del cliente en consola
        return self.mostrar_info()
