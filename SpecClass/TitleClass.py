from tabulate import tabulate


class TitleClass:

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
