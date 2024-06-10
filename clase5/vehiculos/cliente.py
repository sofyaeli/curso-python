"""
Contiene las funciones para gestionar las reservas y guardarlas en el excel.

`crear_reservas(cliente,vehiculo,fecha_inicio,fecha_final)` : Creamos un diccionario con la informacion de la reserva.

`mostrar_reserva(reserva)` : Devolver en un string la reserva.

`guardar_reserva_en_excel(reservas,archivo)` : Guardar la lista de reservas en el excel.
 

"""


def crear_cliente(nombre,apellido,licencia_conducir):
    return{
        "nombre":nombre,
        "apellido":apellido,
        "licencia_conducir": licencia_conducir
    }

def mostrar_cliente(cliente):
    return f"{cliente["nombre"]} {cliente["apellido"]}, Licencia: {cliente["licencia_conducir"]}"
