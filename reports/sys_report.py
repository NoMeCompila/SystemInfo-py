import os
from datetime import datetime
import jinja2
import pdfkit
import socket
import psutil
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
    information_dict = {
        'current_date': get_current_date(),
        'current_time': get_current_time(),
        'pc_name': get_pc_name(),
        'private_ip': get_private_ip(),
        'public_ip': get_public_ip(),
        'os': get_os(),
        'system_version': get_system_version(),
        'system_architecture': get_architecture(),
        'cpu': get_processor(),
        'physical_cores': get_physical_cores(),
        'logical_cores': get_logical_cores(),
        'total_ram': get_total_ram(),
        'used_ram': get_used_ram(),
        'free_ram': get_free_ram(),
        'gpu_id': get_gpu_id(),
        'gpu_name': get_gpu_name(),
        'gpu_charge': get_gpu_charge(),
        'gpu_free_memory': get_gpu_free_memory(),
        'gpu_used_memory': get_gpu_used_memory(),
        'gpu_total_memory': get_gpu_total_memory(),
        'gpu_temperature': get_gpu_temperature()
    }

    return information_dict


def config_options() -> dict:
    """
    Configuración de opciones para wkhtmltopdf
    :return: dict
    """
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.50in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'no-outline': None
    }

    return options


def config_css() -> str:
    """
    Configuración de la ruta del archivo CSS
    :return: str
    """
    return './style.css'


def config_pdfkit() -> pdfkit.configuration:
    """
    Configuración de la ubicación de wkhtmltopdf
    :return: pdfkit.configuration
    """
    return pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")


def report_output_path() -> str:
    """
    Configuración de la ruta de salida del PDF
    :return: str
    """
    return os.path.join(os.path.dirname('.'), 'sys_report.pdf')


def html_output_path(html_report_path: str, information: dict) -> str:
    """
    Configuración de la ruta de salida del HTML
    :param html_report_path: str
    :param information: dict
    :return: str
    """
    # Obtén la ruta del directorio del informe HTML
    html_report_dir = os.path.dirname('.')

    # Carga el contenido del informe HTML usando Jinja2
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(html_report_dir))
    template = env.get_template(os.path.basename(html_report_path))
    return template.render(information)


def make_pdf(html_report_path: str, information: dict) -> None:
    """
    Crea un pdf a partir de un html
    :param html_report_path: str
    :param information: dict
    :return: None
    """

    # Ruta de salida para el PDF
    output_path = report_output_path()

    try:
        # Genera el PDF a partir del HTML
        pdfkit.from_string(
            html_output_path(html_report_path, information),
            output_path,
            css=config_css(),
            options=config_options(),
            configuration=config_pdfkit()
        )
    except Exception:
        print(f"Reporte Generado")


if __name__ == '__main__':
    report_path = r'C:\Users\FeR\Desktop\AllProjects\pySPECs-master\reports\template.html'
    info = fill_info_dict()
    try:
        make_pdf(report_path, info)
    except Exception as e:
        print(f"Repoerte generado")
