import os
from datetime import datetime
from tabulate import tabulate


def get_current_time() -> str:
    """
    Retorna la hora actual en formato hh:mm:ss
    :return: str
    """
    return datetime.now().strftime("%H:%M:%S")


def get_current_date() -> str:
    """
    Retorna la fecha actual en formato dd/mm/aaaa
    :return: str
    """
    return datetime.now().strftime("%d/%m/%Y")


def get_all_installed_programs(directory: str) -> list:
    """
    Retorna una lista de diccionarios con la informacion de los programas instalados
    :param directory:
    :return: list
    """
    programs = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            program_path = os.path.join(root, file)
            # Verificamos que el archivo sea ejecutable y que termine en .exe
            if os.access(program_path, os.X_OK) and file.lower().endswith('.exe'):
                # Obtener el tamaño del programa en bytes
                program_size = os.path.getsize(program_path)
                creation_time = datetime.fromtimestamp(os.path.getctime(program_path))
                # Agregamos la información a la lista de programas
                programs.append({
                    'name': file,
                    'path': program_path,
                    'size': program_size,
                    'created at': creation_time
                })
    return programs


def all_installed_programs(directory1: str, directory2: str) -> list:
    """
    Recibe como parametro dos directorios y retorna una lista de diccionarios con la informacion de los programas
    en los directorios de program files y el de program files (x86) para obtener una sola lista de programas
    :param directory1:
    :param directory2:
    :return: list
    """
    return get_all_installed_programs(directory1) + get_all_installed_programs(directory2)


if __name__ == "__main__":
    for program in all_installed_programs("C:\\Program Files (x86)", "C:\\Program Files"):
        head = ("NOMBRE", "RUTA", "TAMAÑO", "FECHA INSTALACIÓN")
        program_list = [[program['name'], program['path'], program['size'], program['created at']]]
        print(tabulate(program_list, headers=head, tablefmt='fancy_grid', stralign='center', floatfmt='.0f'))
        print()

