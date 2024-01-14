import socket
from urllib import request

from SpecClass.TitleClass import TitleClass


class IpClass(TitleClass):

    @staticmethod
    def get_private_ip() -> str:
        """
        Retorna la ip privada del pc
        :return: str
        """
        pc_name = socket.gethostname()
        return str(socket.gethostbyname(pc_name))

    @staticmethod
    def get_public_ip() -> str:
        """
        Retorna la ip publica del pc
        :return: str
        """
        return str(request.urlopen('https://ident.me').read().decode('utf8'))

    def print_ip_table(self) -> None:
        """
        Imprime una tabla con el nombre del pc, la ip privada y la ip publica
        :return: None
        """
        title = TitleClass()
        ifo_list = [self.get_private_ip(), self.get_public_ip()]

        head_tuple = ("IP Privada","IP Pública")
        title.print_table(title.print_title("INFORMACIÓN DEL IP"), ifo_list, head_tuple)