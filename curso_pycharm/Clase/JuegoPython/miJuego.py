import pygame
import random

pygame.init() #inicializamos el entorno
print('Inicializando')
ancho = 640
alto = 480

screen = pygame.display.set_mode((ancho, alto)) #establecemos las medidas de la pantalla que vamos a mostrar al usuario

pygame.display.set_caption('Juego de Gabriel')

#colores
color_azul = pygame.Color(10,10,150)
color_cuadrado = pygame.Color('red')
color_ball = pygame.Color('#006600')


#geometria
x_cuadrado = ancho // 2 #coordenadas del objeto inicial (cuadrado)
y_cuadrado = alto // 2

ancho_cuadrado = 50
alto_cuadrado = 50

#posicion de inicio de la pelota
x_ball = random.randrange(0,ancho)
y_ball = random.randrange(0,alto)

#tamaño de la pelota
radio_ball = 20

#velocidad de moviemiento de la pelota
vx_ball = random.randrange(5,10)
vy_ball = random.randrange(5,10)

#controlamos los fps (refresco pantalla)
clock = pygame.time.Clock()

miImagen = pygame.image.load('./img/fondo.png') #cargo la imagen
pygame.mixer.music.load('./music/musicon.mp3') #cargo el sonido

running = True
pygame.mixer.music.play()

while running:
    #entrada usuario
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Evento de salida')
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                print('Pulsada la tecla de escape')
                running = False
            elif event.key == pygame.K_UP and y_cuadrado > 0:
                print('Pulsado UP')
                y_cuadrado -= 10
            elif event.key == pygame.K_DOWN and y_cuadrado < alto - alto_cuadrado:
                print('Pulsado DOWN')
                y_cuadrado += 10
            elif event.key == pygame.K_LEFT and  x_cuadrado > 0:
                print('Pulsado LEFT')
                x_cuadrado -= 10
            elif event.key == pygame.K_RIGHT and x_cuadrado < ancho - ancho_cuadrado:
                print('Pulsado RIGTH')
                x_cuadrado += 10
            print(x_cuadrado,y_cuadrado)
            
    #actualizamos
            
    x_ball = x_ball + vx_ball #damos movimiento a la pelota imprimiendole una velocidad
    y_ball = y_ball + vy_ball
    
    if x_ball > ancho -radio_ball or x_ball < radio_ball:
        vx_ball = -vx_ball
        
    if y_ball > alto-radio_ball or y_ball < radio_ball:
        vy_ball = -vy_ball
    
    #detección de colisiones
        
    if x_cuadrado < x_ball < x_cuadrado + ancho_cuadrado   and y_cuadrado < y_ball < y_cuadrado + alto_cuadrado:
        print('Hay colision')
        vx_ball = -vx_ball
        vy_ball = -vy_ball
        
    #repintamos en orden inverso a la cercania

    screen.fill(color_azul) #establecemos el fondo en azul
    screen.blit(miImagen,(0,alto-400)) #dibujamos la imagen
    pygame.draw.circle(screen, color_ball, (x_ball,y_ball),radio_ball)
    pygame.draw.rect(screen, color_cuadrado, (x_cuadrado,y_cuadrado,ancho_cuadrado,alto_cuadrado))
    
    pygame.display.flip() #hacemos el intercambio de pantallas.
    
    clock.tick(60) #medir tiempo entre actualizaciones
    
            

#cuando hemos terminado eliminamos los recursos
print('Saliendo')
print(f'{clock.get_fps()} fps')
pygame.quit()