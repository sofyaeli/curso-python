# """
# vehiculos/reservas.py:

# Contiene las funciones para gestionar las reservas y guardarlas en el excel.

# ● `crear_reservas(cliente,vehiculo,fecha_inicio,fecha_final)` : Creamos un diccionario con la informacion de la reserva.

# ● `mostrar_reserva(reserva)` : Devolver en un string la reserva.

# ● `guardar_reserva_en_excel(reservas,archivo)` : Guardar la lista de reservas en el excel.


# """

from datetime import datetime
import pandas as pd

def crear_reservas(cliente,vehiculo,fecha_inicio,fecha_final):
    return {
        "cliente":cliente,
        "vehiculo": vehiculo,
        "fecha_inicio": fecha_inicio,
        "fecha_final": fecha_final,
        "fecha_reserva": datetime.now()
    }


def mostrar_reserva(reserva):


def guardar_reserva_en_excel(reserva,archivo):