import psutil

from SpecClass.TitleClass import TitleClass


class DiskClass(TitleClass):

    def get_disk_info(self) -> list:
        """
        Retorna una lista con la información de los discos
        :return: list
        """
        partitions = psutil.disk_partitions()
        titles = [
            [
                'device: ' + part[1],
                'total: ' + self.get_size(psutil.disk_usage(part.mountpoint)[0]),
                'usado: ' + self.get_size(psutil.disk_usage(part.mountpoint)[1]),
            ] for part in partitions
        ]
        return titles

    def print_disk_table(self) -> None:
        """
        Imprime una tabla con la información de los discos
        :return: None
        """

        title = TitleClass()

        info_list = self.get_disk_info()

        # flat_list = list(itertools.chain(*info_list))
        head_tuple = ("Device 1", "Device 2", "Device 3")
        title.print_table(title.print_title("INFORMACIÓN DISCOS"), info_list, head_tuple)
