# importo matplotlib para la generación de
# gráficos para mostrar el resultado final
import matplotlib.pyplot as plt

# Variables que utilizaremos
contador = 0
suma = 0
# Inicializo el límite a false para en caso de
# que sea necesario usarlo en su valor True
limite = False
# Guardo los valores en un array
valores = []
# Empiezo el programa pidiendo al usuario los límites
limiteInferior = int(input("Introduce el límite inferior: "))
limiteSuperior = int(input("Introduce el límite superior: "))

# compruebo que el límite inferior no sea mayor que el límite superior
# si es así informo y vuelvo a pedir los valores
while limiteInferior > limiteSuperior:
  print("El mínimo no puede ser superior al máximo\n")
  limiteInferior = int(input("Introduce el mínimo: "))
  limiteSuperior = int(input("Introduce el máximo: "))

# Compruebo el objetivo del ejercicio recordando
# que si introduce 0 el programa finaliza
valor = int(input("Introduce un valor (0 para salir)\n"))
while valor != 0:
  if valor >= limiteInferior and valor<=limiteSuperior:
    suma += valor
    valores.append(valor)
  else:
    contador += 1
    if valor == limiteInferior or valor == limiteSuperior:
      limite = True
  valor = int(input("Introduce un valor (0 para salir)\n"))

# muestro el resultado finall en pantalla
print("La suma de los números es: ", suma)
print("Los valores fuera del intervalo son: ", contador)

# Compruebo si algún valor introducido es igual a un límite
if valor==limite:
  print("Información!!")
  print("Hay valores igual a los límites")
else:
  print("Información!!")
  print("No hay valores igual a los límites")

# Uso el gráfico para visualizar el resultado
# Le doy valor tanto al eje x como al eje y
plt.plot(valores)
plt.xlabel('ejecución')
plt.ylabel('valor')
plt.grid()

# Finalmente muestro el gráfico
plt.show()