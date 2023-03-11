import schedule

#importo la libreria para en futuras llamadas podamos llamar a todas las funciones de datetime
from datetime import datetime

#importamos la libreria sleep
from time import sleep

#importamos el archivo de la copia
import copiaSeguridadSemanal
import webScraping2

def tarea():
    print('Ejecutando la tarea', datetime.now())

def tarea2():
    print('Ejecutando la tarea 2', datetime.now())
    
#ejecutamos una tarea cada 5 segundos
schedule.every(3).seconds.do(tarea)

#ejecutamos la tarea2 cada minuto
schedule.every(6).seconds.do(tarea2)

#ejecutamos la copia de seguridad de forma semanal
tarea_copia = schedule.every().saturday.do(copiaSeguridadSemanal.copiaSeguridadSemanal)
#prueba
#tarea_resultados = schedule.every().second.do(webScraping2.resultados)
tarea_resultados = schedule.every().day.do(webScraping2.resultados)

#le digo que este siempre ejecutando las tareas
while True:
    schedule.run_pending()
    #print('Pendiente de ejecutar tarea')
    #reviso los trabajos que están pendientes
    tareas_pendientes = schedule.get_jobs()
    print(f'Comprobando {len(tareas_pendientes)} tareas pendientes', datetime.now(), end='\r')
    schedule.cancel_job(tarea_copia)
    sleep(1)