import pygame

#Creacion de ventana de videojuego
pygame.init()

ventana = pygame.display.set_mode((630,517))
pygame.display.set_caption("Ejercicio 1")

#Juego
jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    ventana.fill((255, 255, 255))
    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
