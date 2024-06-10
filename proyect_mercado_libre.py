import requests
from bs4 import BeautifulSoup
import time
import pandas as pd


base_url = "https://listado.mercadolibre.com.ec/computacion-notebooks"



def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        resultado = func(*args, **kwargs)
        end = time.time()
        print(f"Tiempo de ejecucion {func.__name__}: {end - start:.4f} segundos")
        return resultado
    return wrapper


@medir_tiempo
def obtener_datos_productos(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    productos=[]  

    
    items= soup.select(".ui-search-result__content-wrapper")
    
    
    for item in items:
        name_element= item.select_one(".ui-search-item__title")
        price_element= item.select_one(".andes-money-amount__fraction")
        
        
        if name_element and price_element:
            name = name_element.get_text(strip=True)
            price = price_element.get_text(strip=True)
            productos.append((name, price))
     
     
    return productos

@medir_tiempo
def obtener_paginas(base_url):
    productos = []
    page = 1
    while True:
        url = f"{base_url}_Desde_{page}"
        nuevos_productos = obtener_datos_productos(url)
        if not nuevos_productos:
            break
        productos.extend(nuevos_productos)
        page += 48
        
    return productos


def procesar_datos(productos):
    datos_procesados = []
    for nombre, precio in productos:
        # Eliminar puntos y convertir a float
        precio = float(precio.replace(".", "").replace(",", "."))
        datos_procesados.append({"Producto": nombre, "Precio": precio})
          
    return datos_procesados

@medir_tiempo
def guardar_datos_en_archivo_csv(datos, archivo):
    df = pd.DataFrame(datos, columns=["Producto", "Precio"])
    df.to_csv(archivo, index=False, encoding="utf-8")
    return df

def estadisticas_precios(df):
    df['Precio'] = df['Precio'].str.replace('.', '').astype(float)
    print(f"Precio promedio: ${df['Precio'].mean():.2f}")
    print(f"Precio mínimo: ${df['Precio'].min():.2f}")
    print(f"Precio máximo: ${df['Precio'].max():.2f}")

            
#ejecutar funciones
productos= obtener_paginas(base_url)
datos_procesados= procesar_datos(productos)
df= guardar_datos_en_archivo_csv(productos, "productos.csv")
estadisticas_precios(df)
    
    

