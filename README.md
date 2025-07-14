# Registro de Servicios del Auto

Este programa sirve para guardar los servicios de mantenimiento que se le hacen a un auto, como cambio de aceite, frenos, kit de distribución, etc. Guarda la marca y modelo del auto, detalle del servicio, costo en $ y la fecha se pone automática. Todo se guarda en un archivo JSON y cada cosa que se hace queda registrada en un archivo de log.

## Requisitos

- Python 3
- Librería externa: colorama

## Instalación

Para instalarlo primero se hace un entorno virtual:

python -m venv venv


### Después se activa:

venv\Scripts\activate

#### Y se instalan las dependencias con:

pip install -r requirements.txt

##### Para correr el programa se hace:

python main.py

##### Después seguir el menú para agregar un servicio, ver la lista, marcar como pagado o eliminar uno. Los datos se guardan en `servicios.json` y las acciones quedan en `registro.log`.

