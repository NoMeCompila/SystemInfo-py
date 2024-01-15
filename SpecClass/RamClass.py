import psutil

from SpecClass.TitleClass import TitleClass


class RamClass(TitleClass):

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
        info_list = [self.get_total_ram(), self.get_used_ram(), self.get_free_ram()]

        head_tuple = ("Ram Total", "Ram usada", "Ram libre")
        title.print_table(title.print_title("INFORMACIÓN LA RAM"), info_list, head_tuple)
