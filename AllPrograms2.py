import os
from datetime import datetime
from tabulate import tabulate


def get_all_installed_programs():
    programs = []
    nro = 0
    program_files_dir = "C:\\Program Files (x86)"  # Ajusta esto según tu sistema operativo
    for root, dirs, files in os.walk(program_files_dir):
        nro += 1
        for file in files:

            program_path = os.path.join(root, file)
            # Verificamos que el archivo sea ejecutable y que termine en .exe
            if os.access(program_path, os.X_OK) and file.lower().endswith('.exe'):
                # Obtener el tamaño del programa en bytes
                program_size = os.path.getsize(program_path)
                creation_time = datetime.fromtimestamp(os.path.getctime(program_path))
                # Agregamos la información a la lista de programas
                programs.append({
                    'nro': nro,
                    'name': file,
                    'path': program_path,
                    'size': program_size,
                    'created at': creation_time
                })

    return programs


if __name__ == "__main__":
    # Obtenemos la lista de todos los programas instalados
    all_installed_programs = get_all_installed_programs()

    # Imprimimos la información de cada programa
    for program in all_installed_programs:
        head = ("ID", "NOMBRE", "RUTA", "TAMAÑO", "FECHA INSTALACIÓN" )
        program_list = [[program['nro'], program['name'], program['path'], program['size'], program['created at']]]
        print(tabulate(program_list, headers=head, tablefmt='fancy_grid', stralign='center', floatfmt='.0f'))
        print()
