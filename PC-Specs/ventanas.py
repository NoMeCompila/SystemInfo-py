import socket
import urllib.request
from tkinter import Label
import platform
import customtkinter
from customtkinter import CTkLabel
import psutil

# set appearance mode and default color theme
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# create CTk window like you do with the Tk window
app = customtkinter.CTk()


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



# def space_in_disc() -> None:
#     """
#     Funcion que devuelve informacion sobre el espacio en disco
#     :return: str
#     """
#
#     partitions = psutil.disk_partitions()
#     for partition in partitions:
#         archivo.write(f"Disco Local: {partition.device}")
#         archivo.write(f"\nPunto de montaje: {partition.mountpoint}")
#         archivo.write(f"\nTipo de archivo del sistema: {partition.fstype}")
#         try:
#             partition_usage = psutil.disk_usage(partition.mountpoint)
#         except PermissionError:
#             continue
#         archivo.write("\nEspacio total en disco: " + get_size(partition_usage.total))
#         archivo.write("\nEspacio usado en disco: " + get_size(partition_usage.used))
#         archivo.write("\nEspacio libre en disco: " + get_size(partition_usage.free))


if __name__ == "__main__":
    # Use CTkButton instead of tkinter Button
    button = customtkinter.CTkButton(master=app, text="Generar PDF", command=button_function, corner_radius=10,
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

    # frame = customtkinter.CTkFrame(master=app, width=600, height=400,fg_color="#1958AA", corner_radius=10)
    # frame.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    tabview = customtkinter.CTkTabview(master=app, width=600, height=400, fg_color="#1F6AA5")
    tabview.pack(padx=20, pady=20)
    tabview.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    tabview.add("IP")
    tabview.add("Sistema")
    tabview.add("RAM")
    tabview.add("Disco")
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




    app.mainloop()
