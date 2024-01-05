import psutil
from tabulate import tabulate
import GPUtil
import socket
import urllib.request
import platform


def print_title(title: str) -> None:
    print("=" * 50, title, "=" * 50)


def get_pc_name() -> str:
    return str(socket.gethostname())


def get_private_ip() -> str:
    pc_name = socket.gethostname()
    return str(socket.gethostbyname(pc_name))


def get_public_ip() -> str:
    return str(urllib.request.urlopen('https://ident.me').read().decode('utf8'))


def print_name_ip_table() -> None:
    print_title('IP INFO')
    ip_info_list = [[get_pc_name(), get_private_ip(), get_public_ip()]]
    head = ('Nombre PC', 'IP privada', 'IP Publica')
    print(tabulate(ip_info_list, headers=head, tablefmt='fancy_grid', stralign='center', floatfmt='.0f'))


def get_os() -> str:
    return platform.architecture()[1]


def get_architecture() -> str:
    return platform.architecture()[0]


def get_system_version():
    return platform.release()


def print_system_table() -> None:
    print_title('SYSTEM INFO')
    system_info_list = [[get_os(), get_architecture(), get_system_version()]]
    head = ('OS', 'Architecture', 'Version')
    print(tabulate(system_info_list, headers=head, tablefmt='fancy_grid', stralign='center', floatfmt='.0f'))


def print_gpu_info_table() -> None:
    print_title('GPU DETAILS')
    gpus = GPUtil.getGPUs()
    list_gpus = []
    for gpu in gpus:
        gpu_id = gpu.id
        gpu_name = gpu.name
        gpu_load = f"{round(gpu.load * 100, 2)}%"
        gpu_free_memory = f"{gpu.memoryFree}MB"
        gpu_used_memory = f"{gpu.memoryUsed}MB"
        gpu_total_memory = f"{gpu.memoryTotal}MB"
        gpu_temperature = f"{gpu.temperature} °C"
        list_gpus.append([gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory, gpu_total_memory,
                          gpu_temperature])
    head = ("id", "nombre", "carga", "memoria libre", "memoria usada", "memoria total", "temperatura")
    print(tabulate(list_gpus, headers=head, tablefmt='fancy_grid', stralign='center', floatfmt='.0f'))


def get_machine_type() -> str:
    return str(platform.machine())


def get_processor() -> str:
    return str(platform.processor())


def get_physical_cores() -> str:
    return str(psutil.cpu_count(logical=False))


def get_logical_cores() -> str:
    return str(psutil.cpu_count(logical=True))


def print_cores_table() -> None:
    print_title('CORES')
    cores_list = [[get_processor(), get_physical_cores(), get_logical_cores()]]
    head = ('Procesador', 'Cores Físiscos', 'Cores Lógicos')
    print(tabulate(cores_list, headers=head, tablefmt='fancy_grid', stralign='center', floatfmt='.0f'))


def get_size(num_bytes: float, suffix="B") -> str:
    factor_conversion = 1024
    for unidad in ["", "K", "M", "G", "T", "P"]:
        if num_bytes < factor_conversion:
            return f"{num_bytes:.2f}{unidad}{suffix}"
        num_bytes /= factor_conversion


def get_total_ram() -> str:
    ram = psutil.virtual_memory()
    return str(get_size(ram.total))


def get_used_ram() -> str:
    ram = psutil.virtual_memory()
    return str(get_size(ram.used))


def get_free_ram() -> str:
    ram = psutil.virtual_memory()
    return str(get_size(ram.available))


def print_ram_table() -> None:
    print_title('RAM INFO')
    ram_list = [[get_total_ram(), get_used_ram(), get_free_ram()]]
    head = ('Ram Total', 'Ram usada', 'Ram libre')
    print(tabulate(ram_list, headers=head, tablefmt='fancy_grid', stralign='center', floatfmt='.0f'))


def get_disk_info() -> list:
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
    print_title('DISK USAGE')
    print(tabulate(get_disk_info(), headers=('Device', 'Total', 'Usado', 'disponible'), tablefmt='fancy_grid'))


if __name__ == '__main__':
    print_name_ip_table()
    print_system_table()
    print_cores_table()
    print_gpu_info_table()
    print_ram_table()
    print_disk_table()
