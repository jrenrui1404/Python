import  requests
from bs4 import BeautifulSoup as bs

def resultados():

    # creamos una variable con la URL
    URL = 'https://www.x-rates.com/table/?from=USD&amount=1'
    
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
        #print(soup)

        #filtro por el contenido que estoy buscando
        valores_salida = soup.find_all('td',attrs={'class':'rtRates'})
        
        #muestro los valores obtenidos de la web x-rates
        print('Euro: ', valores_salida[0].text)
        print('British: ', valores_salida[2].text)
        print('Indian Rupee: ', valores_salida[4].text)
        print('Australian Dollar: ', valores_salida[6].text)
        print('Canadian Dollar: ', valores_salida[8].text)
        print('Singapore Dollar: ', valores_salida[10].text)
    
        f = open("resultados.txt", "w")
        f.write('Euro: ' + valores_salida[0].text)
        f.write('\nBritish: ' + valores_salida[2].text)
        f.write('\nAustralian Dollar:' + valores_salida[4].text)
        f.write('\nIndian Rupee:' + valores_salida[6].text)
        f.write('\nCanadian Dollar: ' + valores_salida[8].text)
        f.write('\nSingapore Dollar: ' + valores_salida[10].text)
        f.write('\n...')