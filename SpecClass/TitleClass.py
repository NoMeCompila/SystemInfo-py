import  socket
from tabulate import tabulate


class TitleClass:

    @staticmethod
    def get_pc_name() -> str:
        """
        Retorna el nombre del pc
        :return: str
        """
        return str(socket.gethostname())

    def get_size(self, num_bytes: float, suffix="B") -> str:
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

    @staticmethod
    def print_title(title: str) -> str:
        """
        Imprime un titulo con un formato especifico
        :param title:
        :return: None
        """

        divisor = "=" * 50
        return divisor + title + divisor

    def print_table(self, custom_title: str, info_list: list, head: tuple) -> None:
        """
        Imprime una tabla con el nombre del pc, la ip privada y la ip publica
        :return: None
        """

        print(self.print_title(custom_title))
        info = [info_list]
        print(tabulate(info, headers=head, tablefmt='fancy_grid', stralign='center', floatfmt='.0f'))
