import socket
from tkinter import *
from tkinter import ttk
import urllib.request
import platform

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


# Iniciar el bucle principal de Tkinter
if __name__ == "__main__":
    # create a windows and set a title
    windows = Tk()
    windows.title('PC-SPECS')

    # arithmetic calculation to always open the windows at the center of the screen
    screen_width = windows.winfo_screenwidth()
    screen_height = windows.winfo_screenheight()
    windows_width = 900
    windows_height = 850
    pos_x = int(screen_width / 2 - windows_width / 2)
    pos_y = int(screen_height / 2 - windows_height / 2)
    windows.geometry(f"{windows_width}x{windows_height}+{pos_x}+{pos_y}")

    # set the windows color
    windows.configure(background="#b186f1")

    # chat text label config
    input_label = Label(windows, text="Especificaciones: " + get_pc_name(), bg="#caacf9")
    input_label.config(fg="black", font=("Roboto", 18))
    input_label.pack(pady=5)

    # ip publica y privada
    input_label = Label(windows,
                        text=f"INFORMMACIÓN DE LA IP\n\nIP Privada: {get_private_ip()}\nIP Publica: {get_public_ip()}",
                        bg="#caacf9")
    input_label.config(fg="black", font=("Roboto", 12))
    input_label.pack(pady=5)

    # SISTEMA
    input_label = Label(windows,
                        text=f"INFORMMACIÓN DEL SISTEMA\n\nSO: {get_private_ip()}\nVersión: {get_public_ip()}\n",
                        bg="#caacf9")
    input_label.config(fg="black", font=("Roboto", 12))
    input_label.pack(pady=5)



    #
    # # text box to enter prompt
    # input_textbox = Text \
    #     (
    #         windows,
    #         height=8,
    #         width=70,
    #         bg="#343541",
    #         fg="white",
    #         font=("Roboto", 12),
    #         highlightthickness=1,
    #         highlightbackground="white"
    #     )
    #
    # input_textbox.pack(pady=10)
    #
    # output_label = Label(windows, text="OUTPUT", bg="#444654")
    # output_label.config(fg="white", font=("Roboto", 12))
    # output_label.pack(pady=5)
    #
    # # create an output textbox
    # output_textbox = Text \
    #     (
    #         windows,
    #         height=18,
    #         width=70,
    #         bg="#343541",
    #         fg="white",
    #         font=("Roboto", 12),
    #         highlightthickness=1,
    #         highlightbackground="white"
    #     )

    # output_textbox.pack(pady=5)

    # Make a custom button
    # button_response = Button(windows, text="Responder", bg="black", fg="white", relief="flat", cursor="hand2", bd=0,
    #                          padx=10,
    #                          command=chat_gpt)

    windows.mainloop()
