import pygame
from random import randint

pygame.init()
ventana = pygame.display.set_mode((630, 410))
pygame.display.set_caption("Ejemplo 4")

fond = pygame.image.load("fondo.png")
fondrect = fond.get_rect()

fondrect.left = 0.1
fondrect.top = 9

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
speed = [randint(3, 6), randint(3, 6)]
ballrect.move_ip(0, 0)

barra = pygame.image.load("barra.png")
barrarect = barra.get_rect()
barrarect.move_ip(340, 385)

bricklist = []
for brick in bricklist:
    brick = pygame.image.load("brick.png")
    brickrect = brick.get_rect()

fuente = pygame.font.Font(None, 150)

jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        barrarect = barrarect.move(-3, 0)
    if keys[pygame.K_RIGHT]:
        barrarect = barrarect.move(3, 0)

    if barrarect.colliderect(ballrect):
        speed[1] = -speed[1]

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0:
        speed[1] = -speed[1]
    if ballrect.bottom > ventana.get_height():
        texto = fuente.render("Game Over", True, (0, 0, 0))
        texto_rect = texto.get_rect()
        texto_x = ventana.get_width() / 2 - texto_rect.width / 2
        texto_y = ventana.get_height() / 2 - texto_rect.height / 2
        ventana.blit(texto, [texto_x, texto_y])
    else:
        ventana.fill((0, 0, 0))
        ventana.blit(fond, fondrect)
        ventana.blit(ball, ballrect)
        ventana.blit(barra, barrarect)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
