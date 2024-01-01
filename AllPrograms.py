import psutil
import os
from datetime import datetime


def get_installed_programs():
    programs = []

    # Iteramos sobre los procesos con información específica
    for proc in psutil.process_iter(['pid', 'name', 'create_time', 'exe']):
        try:
            # Extraemos información del proceso
            program_name = proc.info['name']
            program_pid = proc.info['pid']
            program_create_time = datetime.fromtimestamp(proc.info['create_time'])

            # Obtenemos la ruta al ejecutable del proceso
            program_exe = proc.info['exe']

            # Verificamos que la ruta al ejecutable no sea None y que exista
            if program_exe is not None and os.path.exists(program_exe):
                # Obtener el tamaño del programa en bytes
                program_size = os.path.getsize(program_exe)

                # Agregamos la información a la lista de programas
                programs.append({
                    'name': program_name,
                    'pid': program_pid,
                    'create_time': program_create_time,
                    'size': program_size
                })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Ignoramos excepciones relacionadas con el acceso a procesos
            pass

    return programs


if __name__ == "__main__":
    # Obtenemos la lista de programas instalados
    installed_programs = get_installed_programs()

    # Imprimimos la información de cada programa
    for program in installed_programs:
        print(f"Nombre: {program['name']}")
        print(f"PID: {program['pid']}")
        print(f"Fecha de Creación: {program['create_time']}")
        print(f"Tamaño: {program['size']} bytes\n")
