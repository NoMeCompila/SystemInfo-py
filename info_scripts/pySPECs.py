import socket  # libreria para saber nombre del PC
import platform  # libreria para obtener especificaciones de hardware
import urllib.request  # libreria para obtener ip publica y privada
import psutil  # libreria para el manejo de memoria
from io import open  # para abrir el archivo
import os  # para manejar archivos y directorios


def pc_name() -> None:
    """
    Funcion que devuelve el nombre de la PC
    :return: str
    """
    name = socket.gethostname()
    archivo.write("Nombre de la PC: " + name)


def private_ip() -> None:
    """
    Funcion que devuelve la IP privada
    :return: str
    """
    name = socket.gethostname()
    priv_ip = socket.gethostbyname(name)
    archivo.write("IP privada: " + priv_ip)


def public_ip() -> None:
    """
    Funcion que devuelve la IP publica
    :return: str
    """
    ip_externa = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    archivo.write("IP publica: " + ip_externa)


def os_system() -> None:
    """
    Funcion que devuelve informacion del sistema
    :return: str
    """
    arqui_sist = platform.architecture()
    archivo.write("Arquitectura y SO: " + str(arqui_sist))
    vers = platform.release()
    archivo.write("\nVersion: " + vers)


def get_cores() -> None:
    """
    Funcion que devuelve informacion sobre el hardware
    :return: str
    """
    tipo_mauina = platform.machine()
    archivo.write("Tipo de maquina: " + tipo_mauina)
    procesador = platform.processor()
    archivo.write("\n" + "Procesador: " + procesador)
    cores_fisicos = psutil.cpu_count(logical=False)
    cores_totales = psutil.cpu_count(logical=True)
    archivo.write("\n" + "cores fisicos: " + str(cores_fisicos) + "\n" + "cores totales: " + str(cores_totales))


def get_size(bytes, sufijo="B") -> str:
    """
    Funcion que devuelve el tamaño de la memoria en formato legible

            Reescala los bytes al formato adecuado
            1253656 => '1.20MB'
            1253656678 => '1.17GB'

    :param bytes: tamaño de la memoria
    :param sufijo: sufijo de la unidad de medida
    :return: str
    """
    factor_conversion = 1024
    for unidad in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor_conversion:
            return f"{bytes:.2f}{unidad}{sufijo}"
        bytes /= factor_conversion


def ram_memory() -> None:
    """
    Funcion que devuelve informacion sobre la memoria RAM
    :return: str
    """
    ram = psutil.virtual_memory()
    archivo.write("\nMemoria RAM  total: " + get_size(ram.total))
    archivo.write("\nMemoria RAM usada: " + get_size(ram.used))
    archivo.write("\nMemoria RAM disponible: " + get_size(ram.available))


def space_in_disc() -> None:
    """
    Funcion que devuelve informacion sobre el espacio en disco
    :return: str
    """
    partitions = psutil.disk_partitions()
    for partition in partitions:
        archivo.write(f"\n=== Disco Local: {partition.device} ===")
        archivo.write(f"\nPunto de montaje: {partition.mountpoint}")
        archivo.write(f"\nTipo de archivo del sistema: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        archivo.write("\nEspacio total en disco: " + get_size(partition_usage.total))
        archivo.write("\nEspacio usado en disco: " + get_size(partition_usage.used))
        archivo.write("\nEspacio libre en disco: " + get_size(partition_usage.free))


# Funcion que une a todas las anteriores y cierra el archivo
def execute_all() -> None:
    archivo.write("=" * 40 + "Nombre PC" + "=" * 40 + "\n")
    pc_name()
    archivo.write("\n" + "=" * 40 + "Informacion IP" + "=" * 40 + "\n")
    private_ip()
    archivo.write("\n")
    public_ip()
    archivo.write("\n" + "=" * 40 + "SISTEMA" + "=" * 40 + "\n")
    os_system()
    archivo.write("\n" + "=" * 40 + "Hardware" + "=" * 40 + "\n")
    get_cores()
    archivo.write("\n" + "=" * 40 + "Memoria RAM" + "=" * 40)
    ram_memory()
    archivo.write("\n" + "=" * 40 + "Memoria en Disco" + "=" * 40)
    space_in_disc()
    archivo.close()


def direcory_and_file_exists() -> None:
    directorio = "pySPECs-master"
    archivo = "info_pc.txt"
    ruta_completa = os.path.join(directorio, archivo)

    if os.path.exists(ruta_completa):
        print(f"El archivo '{archivo}' fue creado con exito.")
    else:
        print(f"El directorio '{directorio}' y/o el archivo '{archivo}' no existen.")


if __name__ == '__main__':
    archivo = open("info_pc.txt", "w")
    execute_all()
    # directorio_actual = os.path.dirname(os.path.abspath(__file__))
    # print(f"El directorio actual es: {directorio_actual}")
