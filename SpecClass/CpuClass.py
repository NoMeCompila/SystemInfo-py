import platform

import psutil

from SpecClass.TitleClass import TitleClass


class CpuClass:

    @staticmethod
    def get_machine_type() -> str:
        """
        Retorna el tipo de maquina
        :return: str
        """
        return str(platform.machine())

    @staticmethod
    def get_processor() -> str:
        """
        Retorna el procesador
        :return: str
        """
        return str(platform.processor())

    @staticmethod
    def get_physical_cores() -> str:
        """
        Retorna los cores fisicos
        :return: str
        """
        return str(psutil.cpu_count(logical=False))

    @staticmethod
    def get_logical_cores() -> str:
        """
        Retorna los cores lógicos
        :return: str
        """
        return str(psutil.cpu_count(logical=True))

    def print_cores_table(self) -> None:
        """
        Imprime una tabla con el sistema operativo, la arquitectura y la version
        :return: None
        """
        title = TitleClass()

        title.print_table(
            title.print_title("INFORMACIÓN DEL CPU"),
            [self.get_machine_type(), self.get_processor(), self.get_physical_cores(), self.get_logical_cores()],
            ("Tipo de Máquina", "Procesador", "Cores físicos", "Cores Lógicos")
        )
