from GPUtil import GPUtil

from SpecClass.TitleClass import TitleClass


class GpuClass(TitleClass):

    def __init__(self, gpus: list):
        self.gpus = GPUtil.getGPUs()

    def get_gpu_id(self) -> int:
        return self.gpus[0].id

    def get_gpu_name(self) -> str:
        return self.gpus[0].name

    def get_gpu_load(self) -> str:
        return f"{self.gpus[0].load}%"

    def get_gpu_free_memory(self) -> str:
        return f"{self.gpus[0].memoryFree}MB"

    def get_gpu_used_memory(self) -> str:
        return f"{self.gpus[0].memoryUsed}MB"

    def get_gpu_total_memory(self) -> str:
        return f"{self.gpus[0].memoryTotal}MB"

    def get_gpu_temperature(self) -> str:
        return f"{self.gpus[0].temperature} °C"

    def print_gpu_info_table(self) -> None:
        """
        Imprime una tabla con la informacion de la gpu
        :return: None
        """

        title = TitleClass()
        info_list = [
            self.get_gpu_id(),
            self.get_gpu_name(),
            self.get_gpu_load(),
            self.get_gpu_free_memory(),
            self.get_gpu_used_memory(),
            self.get_gpu_total_memory(),
            self.get_gpu_temperature()
        ]

        head_tuple = ("id", "nombre", "carga", "memoria libre", "memoria usada", "memora total", "temperatura")
        title.print_table(title.print_title("INFORMACIÓN DEL GPU"), info_list, head_tuple)
