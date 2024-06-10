"""
Contiene las siguientes funciones para almacenar vehiculos

● `crear_vehiculo(matricula,modelo,precio__por__dia)` Crear un diccionario con la informacion del vehiculo

● `mostrar_vehiculo(vehiculo)` Devuelve una representacion en cadena del vehiculo.

● `alquilar_vehiculo(vehiculo)` Marca el vehiculo como "No Disponible"

● `devolver_vehiculo(vehiculo)` Marca el vehiculo como "Disponible".
 
"""

def crear_vehiculo(matricula,modelo,precio_por_dia):
    return {
        "matircula":matricula,
        "modelo":modelo,
        "preico_por_dia":precio_por_dia,
        "disponible": True
    }


def mostrar_vehiculo(vehiculo):



def alquilar_vehiculo(vehiculo):



def devolver_vehiculo(vehiculo):