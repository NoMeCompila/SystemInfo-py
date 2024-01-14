import psutil
from tabulate import tabulate
import GPUtil
import socket

from SpecClass.CpuClass import CpuClass
from SpecClass.GpuClass import GpuClass
from SpecClass.IpClass import IpClass
from SpecClass.RamClass import RamClass
from SpecClass.SystemClass import SystemClass


def print_title(title: str) -> None:
    """
    Imprime un titulo con un formato especifico
    :param title:
    :return: None
    """
    print("=" * 50, title, "=" * 50)


def get_pc_name() -> str:
    """
    Retorna el nombre del pc
    :return: str
    """
    return str(socket.gethostname())


def print_ip_info() -> None:
    """
    Imprime una tabla con el nombre del pc, la ip privada y la ip publica
    :return: None
    """
    ip = IpClass()
    ip.print_ip_table()


def print_system_info() -> None:
    """
    Imprime una tabla con el sistema operativo, la arquitectura y la version
    :return: None
    """
    system = SystemClass()
    system.print_system_table()


def print_cpu_info() -> None:
    """
    Imprime una tabla con la información de  Tipo de Máquina, Procesador, Cores físicos y los Cores Lógicos
    :return: None
    """
    cpu = CpuClass()
    cpu.print_cores_table()


def print_ram_info() -> None:
    """
    Imprime una tabla con la información de la ram
    :return: None
    """
    ram = RamClass()
    ram.print_ram_table()


def print_gpu_info() -> None:
    """
    Imprime una tabla con la informacion de la gpu
    :return: None
    """

    gpu = GpuClass(GPUtil.getGPUs())
    gpu.print_gpu_info_table()


def get_size(num_bytes: float, suffix="B") -> str:
    """
    Retorna el tamaño en bytes, kilobytes, megabytes, gigabytes, terabytes y petabytes
    :param num_bytes: float
    :param suffix: str
    :return: str
    """
    factor_conversion = 1024
    for unidad in ["", "K", "M", "G", "T", "P"]:
        if num_bytes < factor_conversion:
            return f"{num_bytes:.2f}{unidad}{suffix}"
        num_bytes /= factor_conversion


def get_disk_info() -> list:
    """
    Retorna una lista con la información de los discos
    :return: list
    """
    partitions = psutil.disk_partitions()
    titles = [
        [
            'device: ' + part[1],
            'total: ' + get_size(psutil.disk_usage(part.mountpoint)[0]),
            'usado: ' + get_size(psutil.disk_usage(part.mountpoint)[1]),
            'disponible: ' + get_size(psutil.disk_usage(part.mountpoint)[1])
        ] for part in partitions
    ]
    return titles


def print_disk_table() -> None:
    """
    Imprime una tabla con la información de los discos
    :return: None
    """
    print_title('DISK USAGE')
    print(tabulate(get_disk_info(), headers=('Device', 'Total', 'Usado', 'disponible'), tablefmt='fancy_grid'))


if __name__ == '__main__':
    # print_ip_info()
    print_system_info()
    print()
    print_cpu_info()
    print()
    print_gpu_info()
    print()
    print_ram_info()
    print()
    print_disk_table()
