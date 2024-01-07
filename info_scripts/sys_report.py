import jinja2
import pdfkit
import psutil
from tabulate import tabulate
import GPUtil
import socket
import urllib.request
import platform


def make_pdf(html_report_path: str, info: dict, css_path='') -> None:
    """
    Crea un pdf a partir de un html
    :param html_template:
    :param pdf_name:
    :return: None
    """
    template_path = html_report_path.split('\\')[-1]
    html_report_path = html_report_path.replace('template_path', '')

    print(template_path)
    print(html_report_path)


if __name__ == '__main__':
    template_path = 'C:\\Users\\FeR\Desktop\\AllProjects\pySPECs-master\\reports\\report.html'
    info = {}
    make_pdf(template_path, info)
