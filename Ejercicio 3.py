import pygame
from random import randint
from Sprites import Ball, Barra, Brick

pygame.init()
ventana = pygame.display.set_mode((630, 517))
pygame.display.set_caption("Ejemplo 4")

fond = pygame.image.load("fondo.png")
fondrect = fond.get_rect()
fondrect.left = 0.1
fondrect.top = 2

# Pelota
ball = Ball(8, "ball.png")
#ballrect = ball.get_rect()
#speed = [randint(3, 6), randint(3, 6)]
#ballrect.move_ip(310, 450)

#Barra
barra = Barra(6, "barra.png")
#barrarect = barra.get_rect()
#barrarect.move_ip(280, 480)


#bricklist
list_ladrillos = []
for pos_x in range(16):
    for pos_y in range(3):
        list_ladrillos.append(Brick(40 * pos_x, 45 * pos_y, "brick.png"))
#brick = pygame.image.load("brick.png")
#brickrect = brick.get_rect()

fuente = pygame.font.Font(None, 150)

jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    #Pulsador de teclas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and barra.rect.left > 0:
            if barra.prev_dir == -1:
                if barra.velocidad < 16:
                    barra.valocidad = barra.velocidad + 0.4
                else:
                    barra.velocidad = 6
                barra.prev_dir = -1
                barra.rect = barra.rect.move(-barra.velocidad, 0)

    if keys[pygame.K_RIGHT] and barra.rect.right < ventana.get_width():
            if barra.prev_dir == 1:
                if barra.velocidad < 16:
                    barra.valocidad = barra.velocidad + 0.4
                else:
                    barra.velocidad = 6
                barra.prev_dir = 1
                barra.rect = barra.rect.move(barra.velocidad, 0)

    #Pelota movimiento
    ball.rect = ball.rect.move([ball.movx * ball.speed, ball.movy * ball.speed])
    if ball.rect.left < 0 or ball.rect.right > ventana.get_width():
        ball.movx = -ball.movx
    if ball.rect.top < 0:
        ball.movy = -ball.movy

    #colision pelota - barra
    if barra.rect.colliderect(ball.rect):
        ball.movy = -ball.movy
        if ball.speed< 20:
            ball.speed = ball.speed + 1


    ventana.fill((0, 0, 0))
    ventana.blit(fond, fondrect)
    ventana.blit(ball.image, ball.rect)
    ventana.blit(barra.image, barra.rect)


    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
