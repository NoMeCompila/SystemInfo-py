import psutil

from SpecClass.TitleClass import TitleClass


class RamClass(TitleClass):

    @staticmethod
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

    def get_total_ram(self) -> str:
        """
        Retorna la ram total
        :return: str
        """
        ram = psutil.virtual_memory()
        return str(self.get_size(ram.total))

    def get_used_ram(self) -> str:
        """
        Retorna la ram usada
        :return: str
        """
        ram = psutil.virtual_memory()
        return str(self.get_size(ram.used))

    def get_free_ram(self) -> str:
        """
        Retorna la ram libre
        :return: str
        """
        ram = psutil.virtual_memory()
        return str(self.get_size(ram.available))

    def print_ram_table(self) -> None:
        """
        Imprime una tabla con la información de la ram
        :return: None
        """
        title = TitleClass()
        ifo_list = [self.get_total_ram(), self.get_used_ram(), self.get_free_ram()]

        head_tuple = ("Ram Total", "Ram usada", "Ram libre")
        title.print_table(title.print_title("INFORMACIÓN LA RAM"), ifo_list, head_tuple)
