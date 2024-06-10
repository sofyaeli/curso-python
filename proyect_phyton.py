import requests
from bs4 import BeautifulSoup
import time
import pandas as pd


base_url = "https://books.toscrape.com/"



def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        resultado = func(*args, **kwargs)
        end = time.time()
        print(f"Tiempo de ejecucion {func.__name__}: {end - start:.4f} segundos")
        return resultado
    return wrapper


@medir_tiempo
def obterner_datos_productos(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    productos=[]  

    
    items= soup.select(".product_pod")
    
    for item in items:
        name_element= item.select_one("h3 a")
        price_element= item.select_one(".price_color")
        
        
        if name_element and price_element:
            name = name_element["title"]
            price = price_element.get_text(strip=True)
            productos.append((name,price))
            
        if not name_element or not price_element:
            continue
        
    return productos

@medir_tiempo
def obtener_paginas(base_url):
    productos=[]
    page=1
    while True:
        url= f"{base_url}/catalogue/page-{page}.html"
        nuevos_productos= obterner_datos_productos(url)
        if not nuevos_productos:
            break
        productos.extend(nuevos_productos)
        page+=1 
        
    return productos
    

#funcion procesar datos
@medir_tiempo
def procesar_datos(productos):
    datos_procesados = []
    for nombre, precio in productos:
        #convertir a float
        precio = float(precio.replace("£", "").replace("Â", ""))
        datos_procesados.append({"Producto": nombre, "Precio": precio})
         
    return datos_procesados

#funcion para obtener datos de todas las paginas




#funcion para escribir los datos un archivo-txt
@medir_tiempo
def guardar_datos_en_archivo_csv(datos,archivo):
    df= pd.DataFrame(datos)
    df.to_csv(archivo, index=False, encoding="utf-8")
    return df

#funcion para realizar estadisticas en precios

def estadisticas_precios(df):
    print(f"precio promedio:  £{df['Precio'].mean():.2f}")
    print(f"precio minimo:  £{df['Precio'].mean():.2f}")
    print(f"precio maximo:  £{df['Precio'].mean():.2f}")

            
            
#ejecutar funciones
productos= obtener_paginas(base_url)
datos_procesados= procesar_datos(productos)
df= guardar_datos_en_archivo_csv(datos_procesados, "productos.csv")
estadisticas_precios(df)
    
    

