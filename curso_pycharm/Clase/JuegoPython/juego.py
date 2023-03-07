#Juego de palas, consiste en intentar que la pelota no toque tu borde, moviendo las flechas izq/dcha para la
#pala de arriba y las teclas A/D para la pala de abajo

import pygame
import random

running = True

print("Inicializando")

#carga inicial del entorno
pygame.init()

puntos1 = 0
puntos2 = 0

ancho = 800
alto = 600

screen = pygame.display.set_mode((ancho,alto))

color_tablero = pygame.Color('grey')

color_barra = pygame.Color('green')

color_ball = pygame.Color('yellow')

pygame.display.set_caption('Juego Clásico Pong')

#geometria
x_barra1 = ancho // 2.5
x_barra2 = ancho // 2.5

y_barra1 =  540

y_barra2 =  40

ancho_barra = ancho // 5
alto_barra = alto // 20

x_ball = random.randrange(0,alto)
y_ball = random.randrange(0,alto)

radio_ball = 20

vx_ball = random.randrange(1,4)

vy_ball = random.randrange(1,4)

logo = pygame.image.load('./images/Pong.jpg')


clock = pygame.time.Clock()

#sonido
ganador = pygame.mixer.Sound('./sounds/ganador.mp3')

gol = pygame.mixer.Sound('./sounds/Gol.mp3')

raqueta = pygame.mixer.Sound('./sounds/Raqueta.mp3')

rebote = pygame.mixer.Sound('./sounds/Rebote.mp3')


while running:
    #leemos entrada usuario (eventos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Evento salida")
            running = False
            exit() 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                print('Pulsada tecla escape')
                running = False
            elif event.key == pygame.K_d and x_barra2 < ancho - ancho_barra:
                x_barra2 += 40
            elif event.key == pygame.K_a and x_barra2 > 0:
                x_barra2 -= 40
            elif event.key == pygame.K_LEFT and x_barra1 > 0:
                x_barra1 -= 40
            elif event.key == pygame.K_RIGHT and x_barra1 < ancho - ancho_barra:
                x_barra1 += 40
           
         
                
   #rebotes
    x_ball = x_ball + vx_ball
    y_ball = y_ball + vy_ball
    
    if x_ball > ancho - radio_ball or x_ball < radio_ball:
        vx_ball = -vx_ball
        pygame.mixer.Sound.play(rebote)
        
    #puntos equipo1
    
    if y_ball > alto - radio_ball:
        pygame.mixer.Sound.play(gol)
        puntos1 = puntos1+1
        print("Puntos para el jugador 1")
        print("Marcador: ", puntos1,"-",puntos2)     
        x_ball = 200
        y_ball = 200
        vx_ball = random.randrange(1,3)
        vy_ball = random.randrange(1,3)
    elif y_ball < radio_ball:
        pygame.mixer.Sound.play(gol)
        puntos2 = puntos2+1
        print("Puntos para el jugador 2")
        print("Marcador: ", puntos1,"-",puntos2)       
        x_ball = 200
        y_ball = 200
        vx_ball = random.randrange(1,3)
        vy_ball = random.randrange(1,3)
        
    #deteccion de colisiones
    
    if (x_barra1 < x_ball < x_barra1+ancho_barra and y_barra1 < y_ball < y_barra1+alto_barra) or (x_barra2 < x_ball < x_barra2+ancho_barra and y_barra2 < y_ball < y_barra2+alto_barra):
        vy_ball = -vy_ball
        pygame.mixer.Sound.play(raqueta)
          
    
    #repintamos
            
    screen.fill(color_tablero) #fondo
     
    screen.blit(logo,(100,125))
    
    pygame.draw.circle(screen, color_ball, (x_ball, y_ball), radio_ball)
    
    pygame.draw.rect(screen,color_barra, (x_barra1,y_barra1,ancho_barra,alto_barra))
    pygame.draw.rect(screen,color_barra, (x_barra2,y_barra2,ancho_barra,alto_barra))
    
    pygame.display.flip()
    
    clock.tick(100)
    
    #actualizacion pantalla del usuario
    if puntos1 == 3:
            pygame.mixer.Sound.play(ganador)
            print("Jugador 1 ganador. Marcador: " , puntos1, " - ", puntos2)
            pygame.time.delay(3000)
            exit()
    if puntos2 == 3:
            pygame.mixer.Sound.play(ganador)      
            print("Jugador 2 ganador. Marcador: " , puntos2, " - ", puntos1)
            pygame.time.delay(3000)
            exit()
    
    #al terminar
print("Saliendo")
pygame.quit()
