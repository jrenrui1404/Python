# creamos una variable con la URL
URL = 'https://www.x-rates.com/table/?from=USD&amount=1'

import  requests
from bs4 import BeautifulSoup as bs

#descargamos la web 
request = requests.get(URL)

#comprobamos que la descarga se ha realizado correctamente
if request.status_code != 200:
    
    print('Error en la descarga')
    
else:
    
    #guardamos el contenido en una variable y la imprimimos
    contenido = request.content
    
    #print(contenido)
    soup = bs(contenido, 'html.parser')
    print(soup)

    #filtro por el contenido que estoy buscando
    valores_salida = soup.find_all('td',attrs={'class':'rtRates'})
    
    #muestro los valores obtenidos de la web x-rates
    print('Euro: ', valores_salida[0].text)
    print('British: ', valores_salida[2].text)
    print('Indian Rupee: ', valores_salida[4].text)
    print('Australian Dollar: ', valores_salida[6].text)
    print('Canadian Dollar: ', valores_salida[8].text)
    print('Singapore Dollar: ', valores_salida[10].text)
    