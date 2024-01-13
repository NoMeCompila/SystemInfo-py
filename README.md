
<h1>
<p align="center">
  Free Range Testers Academy January Challenge
</p>
</h1>
<p align="center">
  <img src="https://img-c.udemycdn.com/user/200_H/69063786_13e8_4.jpg" alt="FRT-img">
</p>
<div align="center">
      <img src="https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/267_Python_logo-512.png" style="width: 40px;">
      <img src="https://upload.wikimedia.org/wikipedia/commons/d/d5/Selenium_Logo.png" style="width: 40px;">
      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Pytest_logo.svg/2048px-Pytest_logo.svg.png" style="width: 50px;">
</div>
<p align="center">
  En este proyecto se pone en práctica selenium webdriver junto con la libreria pytest para realizar la automatización de pruebas de busquedas en wikipedia.
</p>

## Descripción del proyecto

Este proyecto surge como primer desafío mensual para la academia de free range testers en el cual el objetivo es ingresar a wikipedia.org y verificar que una busqueda sobre un tema en especifico de los resultados esperados.

## Lenguajes y librerías utilizadas
- python 3.10
- selenium
- pytest
- webdriver-manager
- pytest-xdist
- pytest-html

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



