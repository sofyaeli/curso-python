import re

def validar_correo(correo):
    # Patrón de expresión regular para validar un correo electrónico
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Comprobación del correo con el patrón
    if re.match(patron, correo):
        return True
    else:
        return False

# Ejemplo de uso
correo_ejemplo = "usuario@example.com"
if validar_correo(correo_ejemplo):
    print("El correo electrónico es válido.")
else:
    print("El correo electrónico no es válido.")
