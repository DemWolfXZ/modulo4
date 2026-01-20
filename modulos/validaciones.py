### Validaciones pedidas: email, teléfono, dirección.###

import re
from modulos.excepciones import EmailInvalidoError, TelefonoInvalidoError, DireccionInvalidaError


def validar_email(email: str) -> bool:
    """
    Validar que el email tenga un formato básico correcto.
    Si no cumple, lanza EmailInvalidoError.
    """
    patron = r"^[A-Za-z0-9_.-]+@[A-Za-z0-9_.-]+\.[A-Za-z0-9_]+$"

    if not re.match(patron, email.strip()):
        raise EmailInvalidoError("Email inválido. Ejemplo válido: nombre@dominio.com")
    return True


def validar_telefono(telefono: str) -> bool:
    """
    Validar que el teléfono contenga solo números y tenga largo razonable.
    Si no cumple, lanza TelefonoInvalidoError.
    """
    t = telefono.strip()
    if not t.isdigit():
        raise TelefonoInvalidoError("Teléfono inválido. Solo se permiten números.")
    if len(t) < 8 or len(t) > 9:
        raise TelefonoInvalidoError("Teléfono inválido. Debe tener entre 8 y 9 dígitos.")
    return True


def validar_direccion(direccion: str) -> bool:
    """
    Validar que la dirección no esté vacía.
    Si no cumple, lanza DireccionInvalidaError.
    """
    d = direccion.strip()
    if d == "":
        raise DireccionInvalidaError("Dirección inválida. No puede estar vacía.")
    return True
