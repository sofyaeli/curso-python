import requests
from bs4 import BeautifulSoup

# URL de la página de MercadoLibre Ecuador para una búsqueda específica (por ejemplo, "laptops")
url = 'https://listado.mercadolibre.com.ec/computacion-notebooks'

# Realiza una solicitud HTTP para obtener el contenido de la página
response = requests.get(url)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    # Parsear el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encuentra todos los elementos de los productos
    items = soup.find_all('div', class_='ui-search-result__content-wrapper')

    for item in items:
        # Obtén el nombre del producto
        product_name = item.find('h2', class_='ui-search-item__title')
        
        # Obtén el precio del producto
        price = item.find('span', class_='andes-money-amount__fraction')

        # Imprime los resultados
        print(f'Producto: {product_name}')
        print(f'Precio: ${price}')
        print('-' * 10)
else:
    print('No se pudo obtener la página')
