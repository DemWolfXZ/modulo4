# modulos/excepciones.py
# Aquí definimos excepciones personalizadas del sistema (tal como pide la consigna).

class EmailInvalidoError(Exception):
    """Se lanza cuando el email no cumple el formato esperado."""
    pass

#########################################################
class TelefonoInvalidoError(Exception):
    """Se lanza cuando el teléfono no cumple el formato esperado."""
    pass

#########################################################
class DireccionInvalidaError(Exception):
    """Se lanza cuando la dirección es vacía o inválida."""
    pass

#########################################################
class ClienteExistenteError(Exception):
    """Se lanza cuando se intenta registrar un cliente duplicado (por email)."""
    pass

#########################################################
class ClienteNoEncontradoError(Exception):
    """Se lanza cuando no se encuentra un cliente por su ID o email."""
    pass

#########################################################
class TipoClienteInvalidoError(Exception):
    """Se lanza cuando el tipo de cliente no corresponde a los permitidos."""
    pass
