import socket

import customtkinter

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
    label = customtkinter.CTkLabel(app, text=f"ESPECIFICACIONES: {get_pc_name()}", text_color="white", font=("Arial", 20))
    label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

    # frame = customtkinter.CTkFrame(master=app, width=600, height=400,fg_color="#1958AA", corner_radius=10)
    # frame.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    tabview = customtkinter.CTkTabview(master=app, width=600, height=400, fg_color="#1F6AA5")
    tabview.pack(padx=20, pady=20)
    tabview.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    tabview.add("tab 1")  # add tab at the end
    tabview.add("tab 2")  # add tab at the end
    tabview.add("tab 3")  # add tab at the end
    tabview.add("tab 4")  # add tab at the end
    tabview.add("tab 5")  # add tab at the end
    tabview.add("tab 6")  # add tab at the end
    tabview.set("tab 1")  # set currently visible tab

    app.mainloop()
