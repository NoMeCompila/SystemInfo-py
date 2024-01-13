
<h1>
<p align="center">
  PC-SPECS
</p>
</h1>

## Descripción del proyecto

Proyecto personal que surge de la necesidad de mejorar mi primer poryecto python en el que me vi involucrado de manera profesional, en concreto es una aplicación de escritorio que detalla las especificaciones de la computadora que estamos utilizando, detalla componentes de hardware como memoria RAM, CPU GPU, etc y tambien detalles del software del sistema operativo, nombre, distribución y version. Permite copiar estos datos drectamente al portapapeles y permite generar un reporte en PDF con los detalles del mismo

## Lenguajes y librerías utilizadas
- python 3.11.3
- Jinja2~=3.1.2
- pdfkit~=1.0.0
- psutil~=5.9.4
- GPUtil~=1.4.0
- tabulate~=0.9.0
- customtkinter~=5.2.1
- pyinstaller~=6.3.0

## Requisitos

- Python 3.x o superior
- Conexión a internet
- ~~Cambiar las rutas absolutas (todavia no descubrí como hacer que funcione en pytest con relative paths)~~
- ya arregle las rutas
### comandos para instalar las librerias necesarias

- entorno virtual de python
```
pip install pipenv
```
- selenium
```
pipenv install selenium
```
- pytest
```
pipenv install pytest
```
- reportes html
```
pipenv install pytest-html
```
- ejecucion en paralelo
```
pipenv install pytest-xdist
```

## Conceptos Utilizados
- POM
- POO
- asserts con pytest
- Data Provider
- Creación de reportes
- Ejecucion de tests en paralelo
- Múltiple Browsers

## Funcionamiento

1) navega a wikipedia.org y verifica el título correcto
2) Se situa en la barra de busqueda y escribe el tema a buscar (Selenium, Appium)
3) Hace click en el boton de la lupa para buscar 
4) Verifica que el título sea el correspondiente al tema buscado
5) Vielve al Homepage y verifica el título

## Instrucciones de uso

Una vez que tenemos todo instalado y configurado podemos setear las opciones de busqueda (archivo data/search_data.json) y también el navegador (archivo Browsers/config.json) 
simplemente cambiamos el valor de la propiedad browser que por defecto viene con Chrome por las demas que acepta ("Edge", "Headless Chrome", "Firefox").
para ejecutar la búsqueda en paralelo de las 3 opciones y generar un reporte html ejecutamos el siguiente script en el entorno virtual de la terminal de python:

```
py.test -m search -n 3 --html=wikireport.html
```
luego de la ejecución nos queda el siguiente archivo donde podemos ver los resultados de la ejecución en detalle y de manera fácil
![image](https://user-images.githubusercontent.com/54701174/221791632-6f9529a7-7818-41ca-b75e-738a83b0a6f9.png)

## Contribuciones

me pueden contactar por el discord de freerangetester aparezco como Fer Caballero y la foto de nirvana o por linkedin que esta en mi inicio de perfil de github  de perfil, soy Jr TAE y recién estoy aprendiendo, 
acepto cualquier sugerencia o crítica constructiva que crean necesario hacerme saber, así como también si quieren preguntarme algo que no sepan de python o selenium 
me pueden contactar  

## Autor

Fernando Caballero 2023 Corrientes Argentina

## Licencia

Usenla como quieran no me importa xd



