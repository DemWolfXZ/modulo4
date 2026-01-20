import csv
import os
import logging

from modulos.cliente_regular import ClienteRegular
from modulos.cliente_premium import ClientePremium
from modulos.cliente_corporativo import ClienteCorporativo
from modulos.excepciones import TipoClienteInvalidoError


def configurar_logger():
    """
    Configura el logger para escribir en logs/app.log
    """
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        filename="logs/app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )


def exportar_clientes_csv(clientes: list, ruta: str):
    """
    Exporta clientes a un archivo CSV.
    """
    os.makedirs(os.path.dirname(ruta), exist_ok=True)

    with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)

        # Cabecera simple y clara
        escritor.writerow(["id", "nombre", "email", "telefono", "direccion", "tipo", "extra"])

        for c in clientes:
            tipo = type(c).__name__
            # Campo "extra" depende del tipo (para no inventar columnas distintas)
            extra = ""
            if tipo == "ClienteRegular":
                extra = str(getattr(c, "descuento", 0.0))
            elif tipo == "ClientePremium":
                extra = str(getattr(c, "puntos", 0))
            elif tipo == "ClienteCorporativo":
                extra = str(getattr(c, "empresa", ""))
            else:
                extra = ""

            escritor.writerow([c.id, c.nombre, c.email, c.telefono, c.direccion, tipo, extra])


def importar_clientes_csv(ruta: str) -> list:
    """
    Importa clientes desde un CSV de entrada.
    Retorna una lista de objetos cliente (de distintos tipos).
    """
    clientes_importados = []

    with open(ruta, mode="r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            cliente_id = int(fila["id"])
            nombre = fila["nombre"]
            email = fila["email"]
            telefono = fila["telefono"]
            direccion = fila["direccion"]
            tipo = fila["tipo"]
            extra = fila.get("extra", "")

            if tipo == "ClienteRegular":
                descuento = float(extra) if extra != "" else 0.0
                clientes_importados.append(ClienteRegular(cliente_id, nombre, email, telefono, direccion, descuento))
            elif tipo == "ClientePremium":
                puntos = int(extra) if extra != "" else 0
                clientes_importados.append(ClientePremium(cliente_id, nombre, email, telefono, direccion, puntos))
            elif tipo == "ClienteCorporativo":
                empresa = extra if extra != "" else "Sin empresa"
                clientes_importados.append(ClienteCorporativo(cliente_id, nombre, email, telefono, direccion, empresa))
            else:
                raise TipoClienteInvalidoError("Tipo de cliente inválido en CSV.")

    return clientes_importados


def generar_reporte_txt(clientes: list, ruta: str):
    """
    Genera un reporte TXT: total y cantidad por tipo.
    """
    os.makedirs(os.path.dirname(ruta), exist_ok=True)

    total = len(clientes)
    regulares = 0
    premium = 0
    corporativos = 0

    for c in clientes:
        tipo = type(c).__name__
        if tipo == "ClienteRegular":
            regulares += 1
        elif tipo == "ClientePremium":
            premium += 1
        elif tipo == "ClienteCorporativo":
            corporativos += 1

    with open(ruta, mode="w", encoding="utf-8") as archivo:
        archivo.write("Resumen del sistema GIC\n")
        archivo.write("========================\n")
        archivo.write(f"Cantidad total de clientes: {total}\n")
        archivo.write(f"Clientes Regular: {regulares}\n")
        archivo.write(f"Clientes Premium: {premium}\n")
        archivo.write(f"Clientes Corporativo: {corporativos}\n")
