import pandas as pd

def leer_archivoexcel(ruta):
    df= pd.read_excel(ruta)
    print("contenido del archivo:")
    print (df.head())
    return df

def escribir_arcihvo_excel(ruta,datos):
    df= pd.DataFrame(datos)
    
    
    df.to_excel(ruta, index=False, engine="openpyxl")
    print(f"Datos escritos en la {ruta}")
    
datos_escritura = {
    "Nombre": ["Carlos", "Elena", "Pedro", "Sofia", "Mariana"],
    "Edad": [32, 29, 27, 26, 35],
    "Profesión": ["Abogado", "Arquitecta", "Médico", "Ingeniera", "Bióloga"],
    "Ciudad": ["Madrid", "Barcelona", "Sevilla", "Valencia", "Bilbao"]
}
ruta_escritura="/Users/cazar/desktop/escritura.xlsx"

escribir_arcihvo_excel(ruta_escritura, datos_escritura)