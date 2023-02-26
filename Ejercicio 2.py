import pygame

#Se añade la pelota a nuestro videojuego
pygame.init()
ventana = pygame.display.set_mode((640, 480))
pygame.display.set_caption("ejercicio 2")
fond = pygame.image.load("fondo.png").convert()
ventana.blit(fond, [5, 5])

ball = pygame.image.load("ball.png")

ballrect = ball.get_rect()
speed = [4, 4]
ballrect.move_ip(0, 0)

brick = pygame.image.load("brick.png")
brickrect = brick.get_rect()
brickrect.move_ip(100, 100)
jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    ballrect = ballrect.move(speed)

    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]

    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speed[1] = -speed[1]

    ventana.fill((0, 100, 0))
    ventana.blit(brick, brickrect)
    ventana.blit(ball, ballrect)
    pygame.display.flip()
    pygame.time.Clock().tick(60)



  #  ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0:
        speed[1] = -speed[1]
    if ball.rect.bottom > ventana.get_height():
        texto = fuente.render("Game Over", True, (0, 0, 0))
        texto_rect = texto.get_rect()
        texto_x = ventana.get_width() / 2 - texto_rect.width / 2
        texto_y = ventana.get_height() / 2 - texto_rect.height / 2
        ventana.blit(texto, [texto_x, texto_y])
    else:

        ventana.fill((0, 0, 0))
        ventana.blit(fond, fondrect)
        ventana.blit(brick, brickrect)
        ventana.blit(ball, ballrect)
 #       ventana.blit(barra, barrarect)

pygame.quit()
