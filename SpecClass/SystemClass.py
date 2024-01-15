import platform

from SpecClass.TitleClass import TitleClass


class SystemClass(TitleClass):
    # def __init__(self):

    @staticmethod
    def get_os() -> str:
        """
        Retorna el sistema operativo
        :return: str
        """
        return platform.architecture()[1]

    @staticmethod
    def get_architecture() -> str:
        """
        Retorna la arquitectura del sistema operativo
        :return: str
        """
        return platform.architecture()[0]

    @staticmethod
    def get_system_version() -> str:
        """
        Retorna la version del sistema operativo
        :return: str
        """
        return platform.release()

    def print_system_table(self) -> None:
        """
        Imprime una tabla con el sistema operativo, la arquitectura y la version
        :return: None
        """
        title = TitleClass()
        info_list = [self.get_os(), self.get_architecture(), self.get_system_version()]
        head_tuple = ("OS", "Architecture", "Version")
        title.print_table(title.print_title("INFORMACIÓN DEL SISTEMA"),info_list, head_tuple)
