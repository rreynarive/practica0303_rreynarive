import pygame
#Añadimos barra
pygame.init()

ventana = pygame.display.set_mode((630, 517))
pygame.display.set_caption("Ejercicio 2")

#pelota
ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
speed = [4,4]
ballrect.move_ip(0,0)

#Barra
bate = pygame.image.load("barre.png")
baterect = bate.get_rect()
baterect.move_ip(240,450)

# Juego
jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        baterect = baterect.move(-3, 0)
    if keys[pygame.K_RIGHT]:
        baterect = baterect.move(3, 0)

    if baterect.colliderect(ballrect):
        speed[1] = -speed[1]

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]

    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speed[1] = -speed[1]

    ventana.fill((255, 243, 207))

    ventana.blit(ball, ballrect)
    ventana.blit(bate, baterect)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()