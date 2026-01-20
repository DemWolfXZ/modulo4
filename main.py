# Menú por consola para CRUD + archivos + reportes + logs.

import logging

from modulos.gestor_clientes import GestorClientes
from modulos.cliente_regular import ClienteRegular
from modulos.cliente_premium import ClientePremium
from modulos.cliente_corporativo import ClienteCorporativo

from modulos.archivos import configurar_logger, exportar_clientes_csv, importar_clientes_csv, generar_reporte_txt

from modulos.excepciones import (
    EmailInvalidoError, TelefonoInvalidoError, DireccionInvalidaError,
    ClienteExistenteError, ClienteNoEncontradoError, TipoClienteInvalidoError
)


###################
#al crear esta funcion se evita repetir codigo en el main solicitando valores tipo entero y texto
def pedir_entero(mensaje: str) -> int:
    """
    Pide un número entero al usuario.
    Si se equivoca, vuelve a pedir.
    """
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error: debes ingresar un número entero.")


def pedir_texto(mensaje: str) -> str:
    """
    Pide texto al usuario.
    """
    return input(mensaje).strip()


##################################

# Crear cliente según tipo elegido en consola
def crear_cliente_por_tipo():
    """
    Crea un cliente según tipo elegido en consola.
    Primero se elige el tipo, y si el usuario se equivoca,
    se vuelve a pedir sin solicitar datos todavía.
    """

    # Pedimos el tipo hasta que sea válido
    while True:
        print("""
            Tipos de cliente disponibles:
            1) ClienteRegular
            2) ClientePremium
            3) ClienteCorporativo       
            """ )

        opcion = pedir_texto("Elige tipo de cliente: (1/2/3): ")

        if opcion in ["1", "2", "3"]:
            break  # Sale del bucle porque ya es válido
        else:
            print("Opción inválida. Debes elegir 1, 2 o 3.\n")

    # Una vez que el tipo es válido, recién pedimos los datos base
    cliente_id = pedir_entero("ID: ")
    nombre = pedir_texto("Nombre: ")
    email = pedir_texto("Email: ")
    telefono = pedir_texto("Teléfono (solo números): ")
    direccion = pedir_texto("Dirección: ")

    # Creamos el objeto según el tipo
    if opcion == "1":
        descuento = pedir_texto("Descuento (ej: 10.5): ")
        descuento_val = float(descuento) if descuento != "" else 0.0
        return ClienteRegular(cliente_id, nombre, email, telefono, direccion, descuento_val)

    if opcion == "2":
        puntos = pedir_texto("Puntos (ej: 100): ")
        puntos_val = int(puntos) if puntos != "" else 0
        return ClientePremium(cliente_id, nombre, email, telefono, direccion, puntos_val)

    if opcion == "3":
        empresa = pedir_texto("Empresa: ")
        empresa_val = empresa if empresa != "" else "Sin empresa"
        return ClienteCorporativo(cliente_id, nombre, email, telefono, direccion, empresa_val)


def mostrar_menu():
    print("\n===== GIC - Gestor Inteligente de Clientes =====")
    print("1) Agregar cliente")
    print("2) Listar clientes")
    print("3) Buscar cliente por ID")
    print("4) Actualizar cliente")
    print("5) Eliminar cliente")
    print("6) Exportar clientes a CSV (datos/clientes.csv)")
    print("7) Importar clientes desde CSV (datos/clientes_entrada.csv)")
    print("8) Generar reporte TXT (reportes/resumen.txt)")
    print("0) Salir")


def main():
    configurar_logger()
    gestor = GestorClientes()

    while True:
        mostrar_menu()
        opcion = pedir_texto("Selecciona una opción: ")

        try:
            if opcion == "1":
                cliente = crear_cliente_por_tipo()
                gestor.agregar_cliente(cliente)
                print("Cliente agregado correctamente.")
                logging.info(f"ALTA cliente: {cliente.email}")

            elif opcion == "2":
                clientes = gestor.listar_clientes()
                if len(clientes) == 0:
                    print("No hay clientes registrados.")
                else:
                    for c in clientes:
                        print(c)  

            elif opcion == "3":
                cid = pedir_entero("Ingresa ID a buscar: ")
                cliente = gestor.buscar_por_id(cid)
                print(cliente)

            elif opcion == "4":
                cid = pedir_entero("Ingresa ID a actualizar: ")
                nuevo_nombre = pedir_texto("Nuevo nombre: ")
                nuevo_email = pedir_texto("Nuevo email: ")
                nuevo_telefono = pedir_texto("Nuevo teléfono: ")
                nueva_direccion = pedir_texto("Nueva dirección: ")

                cliente = gestor.actualizar_cliente(cid, nuevo_nombre, nuevo_email, nuevo_telefono, nueva_direccion)
                print("Cliente actualizado correctamente.")
                logging.info(f"UPDATE cliente ID={cid}")

            elif opcion == "5":
                cid = pedir_entero("Ingresa ID a eliminar: ")
                cliente = gestor.eliminar_cliente(cid)
                print("Cliente eliminado correctamente.")
                logging.info(f"BAJA cliente: {cliente.email}")

            elif opcion == "6":
                exportar_clientes_csv(gestor.listar_clientes(), "datos/clientes.csv")
                print("Exportación realizada en datos/clientes.csv")
                logging.info("EXPORT CSV realizado")

            elif opcion == "7":
                nuevos = importar_clientes_csv("datos/clientes_entrada.csv")
                agregados = 0

                for c in nuevos:
                    try:
                        gestor.agregar_cliente(c)
                        agregados += 1
                    except ClienteExistenteError:
                        # Si viene repetido, no botamos todo el proceso
                        logging.warning(f"Import: cliente duplicado ignorado {c.email}")

                print(f"Importación lista. Clientes agregados: {agregados}")
                logging.info(f"IMPORT CSV realizado - agregados={agregados}")

            elif opcion == "8":
                generar_reporte_txt(gestor.listar_clientes(), "reportes/resumen.txt")
                print("Reporte generado en reportes/resumen.txt")
                logging.info("REPORTE TXT generado")

            elif opcion == "0":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida.")

        except (EmailInvalidoError, TelefonoInvalidoError, DireccionInvalidaError) as err:
            print(f"Error de validación: {err}")
            logging.error(f"VALIDACION: {err}")

        except (ClienteExistenteError, ClienteNoEncontradoError, TipoClienteInvalidoError) as err:
            print(f"Error: {err}")
            logging.error(f"SISTEMA: {err}")
        except FileNotFoundError as err:
            print(f"Error: archivo no encontrado -> {err}")
            logging.error(f"ARCHIVO: {err}")

        except PermissionError as err:
            print(f"Error: permisos insuficientes -> {err}")
            logging.error(f"PERMISOS: {err}")   
        except Exception as err:
            # Captura general para que el sistema no se caiga
            print(f"Ocurrió un error inesperado: {err}")
            logging.error(f"INESPERADO: {err}")


if __name__ == "__main__":
    main()
