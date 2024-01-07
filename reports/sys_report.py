import os
import jinja2
import pdfkit

def make_pdf(html_report_path: str, info: dict, css_path='./style.css') -> None:
    """
    Crea un pdf a partir de un html
    :param html_report_path: str
    :param info: dict
    :return: None
    """

    # Obtén la ruta del directorio del informe HTML
    html_report_dir = os.path.dirname('.')

    # Carga el contenido del informe HTML usando Jinja2
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(html_report_dir))
    template = env.get_template(os.path.basename(html_report_path))
    html_out = template.render(info)

    # Configuración de opciones para wkhtmltopdf
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'no-outline': None
    }

    # Configuración de la ubicación de wkhtmltopdf
    config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

    # Ruta de salida para el PDF
    output_path = os.path.join(html_report_dir, 'sys_report.pdf')

    try:
        # Genera el PDF a partir del HTML
        pdfkit.from_string(html_out, output_path, css=css_path, options=options, configuration=config)
        print(f"El PDF ha sido generado con éxito: {output_path}")
    except Exception as e:
        print(f"Error al generar el PDF: {e}")


if __name__ == '__main__':
    report_path = 'C:\\Users\\FeR\\Desktop\\AllProjects\\pySPECs-master\\reports\\template.html'
    info = {"pc_name": "PC-Fer"}

    # Llama a la función make_pdf y maneja cualquier excepción
    try:
        make_pdf(report_path, info)
    except Exception as e:
        print(f"Error general: {e}")
