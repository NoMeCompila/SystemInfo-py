import GPUtil
import socket

from SpecClass.CpuClass import CpuClass
from SpecClass.DiskClass import DiskClass
from SpecClass.GpuClass import GpuClass
from SpecClass.IpClass import IpClass
from SpecClass.RamClass import RamClass
from SpecClass.SystemClass import SystemClass
from SpecClass.TitleClass import TitleClass


def print_pc_title() -> None:
    """
    Imprime un titulo con el nombre de la PC
    :return:
    """
    title = TitleClass()
    #print(title.get_pc_name())
    print()
    print(f"""
        **************************************************
        |ESPECIFICACIONES DE LA TERMINAL: {title.get_pc_name()}|
        ************************************************** 
    """)
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


def print_disk_info() -> None:
    """
    Recorre la lista de discos Físicos y enumera sus caracteristicas principales
    :return: None
    """
    disk = DiskClass()
    disk.print_disk_table()


if __name__ == '__main__':
    print_pc_title()
    print()
    # print_ip_info()
    # print()
    print_system_info()
    print()
    print_cpu_info()
    print()
    print_gpu_info()
    print()
    print_ram_info()
    print()
    print_disk_info()
