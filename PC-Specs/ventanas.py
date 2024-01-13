import socket
import urllib.request
from tkinter import Label
import platform
import customtkinter
from GPUtil import GPUtil
from customtkinter import CTkLabel
import psutil
import os
from datetime import datetime
import jinja2
import pdfkit
import socket
import psutil
import GPUtil
import urllib.request
import platform


# set appearance mode and default color theme
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# create CTk window like you do with the Tk window
app = customtkinter.CTk()

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

def button_function():
    print("button pressed")


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


def copy_text_from_label(label: CTkLabel):
    """
    Copia el texto de un label
    :param label: Label
    :return: None
    """
    contenido = label.cget("text")
    app.clipboard_clear()
    app.clipboard_append(contenido)
    app.update()


def button_event():
    print("button pressed")

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
    return str(f"{round_to_2_floats(gpus[0].load) * 100}%")


def round_to_2_floats(num: float) -> float:
    """
    Redondea a 2 decimales
    :param num: float
    :return: float
    """
    return round(num, 2)


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


def execute_pdf():
    report_path = r'C:\Users\FeR\Desktop\AllProjects\pySPECs-master\PC-Specs\template.html'
    info = fill_info_dict()
    try:
        make_pdf(report_path, info)
        open_pdf()
    except Exception:
        pass
#        print(f"Repoerte generado")


def open_pdf():
    os.system(r"start C:\Users\FeR\Desktop\AllProjects\pySPECs-master\PC-Specs\sys_report.pdf")


if __name__ == "__main__":
    # Use CTkButton instead of tkinter Button
    button = customtkinter.CTkButton(master=app, text="Generar PDF", command=execute_pdf, corner_radius=10,
                                     border_width=2, height=50, font=("Arial", 20))

    button.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)

    # titulo de la ventana
    app.title("PC-SPECS")

    # tamaño de ventana
    # arithmetic calculation to always open the windows at the center of the screen
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    windows_width = 900
    windows_height = 800
    pos_x = int(screen_width / 2 - windows_width / 2)
    pos_y = int(screen_height / 2 - windows_height / 2)
    app.geometry(f"{windows_width}x{windows_height}+{pos_x}+{pos_y}")

    # titulo del programa
    pc_name_label = customtkinter.CTkLabel(app, text=f"ESPECIFICACIONES: {get_pc_name()}", text_color="white",
                                   font=("Arial", 20))
    pc_name_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

    # Botón que copia el nombre de la PC
    copy_name_btn = customtkinter.CTkButton(app, text="Copy", command=lambda: copy_text_from_label(pc_name_label))
    copy_name_btn.place(relx=0.5, rely=0.15, anchor=customtkinter.CENTER)


    tabview = customtkinter.CTkTabview(master=app, width=600, height=400, fg_color="#1F6AA5")
    tabview.pack(padx=20, pady=20)
    tabview.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    tabview.add("IP")
    tabview.add("Sistema")
    tabview.add("RAM")
    # tabview.add("Disco")
    tabview.add("CPU")
    tabview.add("GPU")
    tabview.set("IP")  # set currently visible tab

    ####################### IP INFO #######################

    # ip publica y privada
    ip_label = customtkinter.CTkLabel(master=tabview.tab("IP"), text=f"INFORMACIÓN DE LA IP", fg_color="#144870",
                                      height=80, font=("Arial", 25), corner_radius=10)
    ip_label.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

    # ip publica
    public_ip_label = customtkinter.CTkLabel(master=tabview.tab("IP"), text=f"IP Pública: {get_public_ip()}",
                                             fg_color="#144870", height=60, font=("Arial", 20), corner_radius=10)
    public_ip_label.place(relx=0.4, rely=0.5, anchor=customtkinter.CENTER)

    # # Botón que copia la ip publica del pc
    copy_ip_btn = customtkinter.CTkButton(master=tabview.tab("IP"), text="Copy",
                                          command=lambda: copy_text_from_label(public_ip_label), corner_radius=10,
                                          border_width=2, height=50, width=30, font=("Arial", 20))

    copy_ip_btn.place(relx=0.7, rely=0.5, anchor=customtkinter.CENTER)

    # ip privada
    private_ip_label = customtkinter.CTkLabel(master=tabview.tab("IP"), text=f"IP Privada: {get_private_ip()}",
                                              fg_color="#144870", height=60, font=("Arial", 20), corner_radius=10)
    private_ip_label.place(relx=0.4, rely=0.7, anchor=customtkinter.CENTER)

    copy_pub_ip_btn = customtkinter.CTkButton(master=tabview.tab("IP"), text="Copy",
                                          command=lambda: copy_text_from_label(public_ip_label), corner_radius=10,
                                          border_width=2, height=50, width=30, font=("Arial", 20))

    copy_priv_ip_btn = customtkinter.CTkButton(master=tabview.tab("IP"), text="Copy",
                                              command=lambda: copy_text_from_label(private_ip_label), corner_radius=10,
                                              border_width=2, height=50, width=30, font=("Arial", 20))

    copy_priv_ip_btn.place(relx=0.7, rely=0.7, anchor=customtkinter.CENTER)


    ####################### SISTEMA OPERATIVO #######################
    # sistema operativo
    os_label = customtkinter.CTkLabel(master=tabview.tab("Sistema"), text=f"SISTEMA OPERATIVO", fg_color="#144870",
                                      height=80, font=("Arial", 25), corner_radius=10)
    os_label.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

    # nombre del sistema operativo
    os_name_label = customtkinter.CTkLabel(master=tabview.tab("Sistema"), text=f"Sistema operativo: {get_os()}",
                                             fg_color="#144870", height=60, font=("Arial", 20), corner_radius=10)
    os_name_label.place(relx=0.4, rely=0.5, anchor=customtkinter.CENTER)

    # version del sistema operativo
    os_version_label = customtkinter.CTkLabel(master=tabview.tab("Sistema"), text=f"Versión: {get_system_version()}",
                                             fg_color="#144870", height=60, font=("Arial", 20), corner_radius=10)
    os_version_label.place(relx=0.4, rely=0.7, anchor=customtkinter.CENTER)

    # arquitectura del sistema operativo
    os_architecture_label = customtkinter.CTkLabel(master=tabview.tab("Sistema"), text=f"Arquitectura: {get_architecture()}",
                                             fg_color="#144870", height=60, font=("Arial", 20), corner_radius=10)
    os_architecture_label.place(relx=0.4, rely=0.9, anchor=customtkinter.CENTER)

    # boton que copia el nombre del sistema operativo
    copy_os_btn = customtkinter.CTkButton(master=tabview.tab("Sistema"), text="Copy",
                                          command=lambda: copy_text_from_label(os_name_label), corner_radius=10,
                                          border_width=2, height=50, width=30, font=("Arial", 20))
    copy_os_btn.place(relx=0.75, rely=0.5, anchor=customtkinter.CENTER)

    # boton que copia la version del sistema operativo
    copy_os_version_btn = customtkinter.CTkButton(master=tabview.tab("Sistema"), text="Copy",
                                          command=lambda: copy_text_from_label(os_version_label), corner_radius=10,
                                          border_width=2, height=50, width=30, font=("Arial", 20))
    copy_os_version_btn.place(relx=0.75, rely=0.7, anchor=customtkinter.CENTER)

    # boton que copia la arquitectura del sistema operativo
    copy_os_architecture_btn = customtkinter.CTkButton(master=tabview.tab("Sistema"), text="Copy",
                                          command=lambda: copy_text_from_label(os_architecture_label), corner_radius=10,
                                          border_width=2, height=50, width=30, font=("Arial", 20))
    copy_os_architecture_btn.place(relx=0.75, rely=0.9, anchor=customtkinter.CENTER)

    ####################### RAM #######################

    # ram
    ram_label = customtkinter.CTkLabel(master=tabview.tab("RAM"), text=f"MEMORIA RAM", fg_color="#144870",
                                      height=80, font=("Arial", 25), corner_radius=10)
    ram_label.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

    # ram total
    ram_total_label = customtkinter.CTkLabel(master=tabview.tab("RAM"), text=f"RAM Total: {get_total_ram()}",
                                             fg_color="#144870", height=60, font=("Arial", 20), corner_radius=10)
    ram_total_label.place(relx=0.4, rely=0.5, anchor=customtkinter.CENTER)

    # ram usada
    ram_used_label = customtkinter.CTkLabel(master=tabview.tab("RAM"), text=f"RAM Usada: {get_used_ram()}",
                                             fg_color="#144870", height=60, font=("Arial", 20), corner_radius=10)
    ram_used_label.place(relx=0.4, rely=0.7, anchor=customtkinter.CENTER)

    # ram libre
    ram_free_label = customtkinter.CTkLabel(master=tabview.tab("RAM"), text=f"RAM Libre: {get_free_ram()}",
                                             fg_color="#144870", height=60, font=("Arial", 20), corner_radius=10)
    ram_free_label.place(relx=0.4, rely=0.9, anchor=customtkinter.CENTER)

    # boton que copia la ram total
    copy_ram_total_btn = customtkinter.CTkButton(master=tabview.tab("RAM"), text="Copy",
                                          command=lambda: copy_text_from_label(ram_total_label), corner_radius=10,
                                          border_width=2, height=50, width=30, font=("Arial", 20))

    copy_ram_total_btn.place(relx=0.75, rely=0.5, anchor=customtkinter.CENTER)

    # boton que copia la ram usada
    copy_ram_used_btn = customtkinter.CTkButton(master=tabview.tab("RAM"), text="Copy",
                                          command=lambda: copy_text_from_label(ram_used_label), corner_radius=10,
                                          border_width=2, height=50, width=30, font=("Arial", 20))

    copy_ram_used_btn.place(relx=0.75, rely=0.7, anchor=customtkinter.CENTER)

    # boton que copia la ram libre
    copy_ram_free_btn = customtkinter.CTkButton(master=tabview.tab("RAM"), text="Copy",
                                          command=lambda: copy_text_from_label(ram_free_label), corner_radius=10,
                                          border_width=2, height=50, width=30, font=("Arial", 20))

    copy_ram_free_btn.place(relx=0.75, rely=0.9, anchor=customtkinter.CENTER)

    ####################### CPU #######################

    # cpu
    cpu_label = customtkinter.CTkLabel(master=tabview.tab("CPU"), text=f"INFORMACIÓN DEL CPU", fg_color="#144870",
                                      height=80, font=("Arial", 25), corner_radius=10)
    cpu_label.place(relx=0.5, rely=0.17, anchor=customtkinter.CENTER)

    # procesador
    processor_label = customtkinter.CTkLabel(master=tabview.tab("CPU"), text=f"Procesador: {get_processor()}",
                                             fg_color="#144870", height=60, font=("Arial", 20), corner_radius=10)
    processor_label.place(relx=0.5, rely=0.42, anchor=customtkinter.CENTER)

    # cores fisicos
    physical_cores_label = customtkinter.CTkLabel(master=tabview.tab("CPU"), text=f"Cores físicos: {get_physical_cores()}",
                                             fg_color="#144870", height=50, font=("Arial", 17), corner_radius=10)
    physical_cores_label.place(relx=0.5, rely=0.75, anchor=customtkinter.CENTER)

    # cores logicos
    logical_cores_label = customtkinter.CTkLabel(master=tabview.tab("CPU"), text=f"Cores lógicos: {get_logical_cores()}",
                                             fg_color="#144870", height=50, font=("Arial", 17), corner_radius=10)

    logical_cores_label.place(relx=0.5, rely=0.93, anchor=customtkinter.CENTER)

    # boton que copia el nombre del procesador
    copy_processor_btn = customtkinter.CTkButton(master=tabview.tab("CPU"), text="Copy", corner_radius=10, border_width=2,
                                                 command=lambda: copy_text_from_label(processor_label))

    copy_processor_btn.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)


    ####################### GPU #######################

    # gpu
    gpu_label = customtkinter.CTkLabel(master=tabview.tab("GPU"), text=f"INFORMACIÓN DE LA GPU", fg_color="#144870",
                                       height=70, font=("Arial", 22), corner_radius=10)
    gpu_label.place(relx=0.5, rely=0.13, anchor=customtkinter.CENTER)

    # nombre de la gpu
    gpu_name_label = customtkinter.CTkLabel(master=tabview.tab("GPU"), text=f"Nombre: {get_gpu_name()}",
                                            fg_color="#144870", height=50, font=("Arial", 18), corner_radius=10)

    gpu_name_label.place(relx=0.5, rely=0.33, anchor=customtkinter.CENTER)

    # porcentaje de uso de la gpu
    gpu_charge_label = customtkinter.CTkLabel(master=tabview.tab("GPU"), text=f"Porcentaje de uso: {get_gpu_charge()}",
                                              fg_color="#144870", height=50, font=("Arial", 18), corner_radius=10)

    gpu_charge_label.place(relx=0.32, rely=0.5, anchor=customtkinter.CENTER)

    # memoria libre de la gpu
    gpu_free_memory_label = customtkinter.CTkLabel(master=tabview.tab("GPU"), text=f"Memoria libre: {get_gpu_free_memory()}",
                                                   fg_color="#144870", height=50, font=("Arial", 18), corner_radius=10)

    gpu_free_memory_label.place(relx=0.71, rely=0.5, anchor=customtkinter.CENTER)

    # # memoria total de la gpu
    gpu_used_memory_label = customtkinter.CTkLabel(master=tabview.tab("GPU"), text=f"Memoria total: {get_gpu_total_memory()}",
                                                    fg_color="#144870", height=50, font=("Arial", 18), corner_radius=10)

    gpu_used_memory_label.place(relx=0.35, rely=0.68, anchor=customtkinter.CENTER)


    # temperatura de la gpu

    gpu_temperature_label = customtkinter.CTkLabel(master=tabview.tab("GPU"), text=f"Temperatura: {get_gpu_temperature()}",
                                                    fg_color="#144870", height=50, font=("Arial", 18), corner_radius=10)

    gpu_temperature_label.place(relx=0.72, rely=0.68, anchor=customtkinter.CENTER)

    app.mainloop()
