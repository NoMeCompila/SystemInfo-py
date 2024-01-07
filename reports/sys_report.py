import os
from datetime import datetime
import jinja2
import pdfkit
import socket
import psutil
from tabulate import tabulate
import GPUtil
import urllib.request
import platform


def get_current_date() -> str:
    """
    Retorna la fecha y hora actual
    :return: str
    """
    return str(datetime.now().strftime("%d/%m/%Y"))


def get_current_time() -> str:
    """
    Retorna la hora actual
    :return: str
    """
    return str(datetime.now().strftime("%H:%M:%S"))


def get_pc_name() -> str:
    """
    Retorna el nombre del pc
    :return: str
    """
    return str(socket.gethostname())


def get_private_ip() -> str:
    """
    Retorna la ip privada del pc
    :return: str
    """
    pc_name = socket.gethostname()
    return str(socket.gethostbyname(pc_name))


def get_public_ip() -> str:
    """
    Retorna la ip publica del pc
    :return: str
    """
    return str(urllib.request.urlopen('https://ident.me').read().decode('utf8'))


def get_os() -> str:
    """
    Retorna el sistema operativo
    :return: str
    """
    return platform.architecture()[1]


def get_system_version() -> str:
    """
    Retorna la version del sistema operativo
    :return: str
    """
    return platform.release()


def get_architecture() -> str:
    """
    Retorna la arquitectura del sistema operativo
    :return: str
    """
    return platform.architecture()[0]


def get_processor() -> str:
    """
    Retorna el procesador
    :return: str
    """
    return str(platform.processor())


def get_physical_cores() -> str:
    """
    Retorna los cores fisicos
    :return: str
    """
    return str(psutil.cpu_count(logical=False))


def get_logical_cores() -> str:
    """
    Retorna los cores lógicos
    :return: str
    """
    return str(psutil.cpu_count(logical=True))


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


def get_total_ram() -> str:
    """
    Retorna la ram total
    :return: str
    """
    ram = psutil.virtual_memory()
    return str(get_size(ram.total))


def get_used_ram() -> str:
    """
    Retorna la ram usada
    :return: str
    """
    ram = psutil.virtual_memory()
    return str(get_size(ram.used))


def get_free_ram() -> str:
    """
    Retorna la ram libre
    :return: str
    """
    ram = psutil.virtual_memory()
    return str(get_size(ram.available))


def get_gpu_id() -> str:
    """
    Retorna el id de la gpu
    :return: str
    """
    gpus = GPUtil.getGPUs()
    return str(gpus[0].id)


def get_gpu_name() -> str:
    """
    Retorna el nombre de la gpu
    :return: str
    """
    gpus = GPUtil.getGPUs()
    return str(gpus[0].name)


def get_gpu_charge() -> str:
    """
    Retorna el porcentaje de uso de la gpu
    :return: str
    """
    gpus = GPUtil.getGPUs()
    return str(f"{gpus[0].load * 100}%")


def get_gpu_free_memory() -> str:
    """
    Retorna la memoria libre de la gpu
    :return: str
    """
    gpus = GPUtil.getGPUs()
    return str(f"{gpus[0].memoryFree}MB")


def get_gpu_used_memory() -> str:
    """
    Retorna la memoria usada de la gpu
    :return: str
    """
    gpus = GPUtil.getGPUs()
    return str(f"{gpus[0].memoryUsed}MB")


def get_gpu_total_memory() -> str:
    """
    Retorna la memoria total de la gpu
    :return: str
    """
    gpus = GPUtil.getGPUs()
    return str(f"{gpus[0].memoryTotal}MB")


def get_gpu_temperature() -> str:
    """
    Retorna la temperatura de la gpu
    :return: str
    """
    gpus = GPUtil.getGPUs()
    return str(f"{gpus[0].temperature} °C")


def fill_info_dict() -> dict:
    """
    Llena un diccionario con la información del sistema
    :return: dict
    """
    information_dict = {}
    information_dict['current_date'] = get_current_date()
    information_dict['current_time'] = get_current_time()
    information_dict['pc_name'] = get_pc_name()
    information_dict['private_ip'] = get_private_ip()
    information_dict['public_ip'] = get_public_ip()
    information_dict['os'] = get_os()
    information_dict['system_version'] = get_system_version()
    information_dict['system_architecture'] = get_architecture()
    information_dict['cpu'] = get_processor()
    information_dict['physical_cores'] = get_physical_cores()
    information_dict['logical_cores'] = get_logical_cores()
    information_dict['total_ram'] = get_total_ram()
    information_dict['used_ram'] = get_used_ram()
    information_dict['free_ram'] = get_free_ram()
    information_dict['gpu_id'] = get_gpu_id()
    information_dict['gpu_name'] = get_gpu_name()
    information_dict['gpu_charge'] = get_gpu_charge()
    information_dict['gpu_free_memory'] = get_gpu_free_memory()
    information_dict['gpu_used_memory'] = get_gpu_used_memory()
    information_dict['gpu_total_memory'] = get_gpu_total_memory()
    information_dict['gpu_temperature'] = get_gpu_temperature()
    return information_dict


def make_pdf(html_report_path: str, info: dict, css_path='./style.css') -> None:
    """
    Crea un pdf a partir de un html
    :param html_report_path: str
    :param info: dict
    :return: None
    """

    # Obtén la ruta del directorio del informe HTML
    html_report_dir = os.path.dirname('.')

    # Carga el contenido del informe HTML usando Jinja2
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(html_report_dir))
    template = env.get_template(os.path.basename(html_report_path))
    html_out = template.render(info)

    # Configuración de opciones para wkhtmltopdf
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.50in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'no-outline': None
    }

    # Configuración de la ubicación de wkhtmltopdf
    config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

    # Ruta de salida para el PDF
    output_path = os.path.join(html_report_dir, 'sys_report.pdf')

    try:
        # Genera el PDF a partir del HTML
        pdfkit.from_string(html_out, output_path, css=css_path, options=options, configuration=config)
        print(f"El PDF ha sido generado con éxito: {output_path}")
    except Exception as e:
        print(f"Error al generar el PDF: {e}")


if __name__ == '__main__':
    report_path = r'C:\Users\FeR\Desktop\AllProjects\pySPECs-master\reports\template.html'
    info = fill_info_dict()

    # Llama a la función make_pdf y maneja cualquier excepción
    try:
        make_pdf(report_path, info)
    except Exception as e:
        print(f"Repoerte generado")
