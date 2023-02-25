import pygame

#Creacion de ventana de videojuego
pygame.init()

ventana = pygame.display.set_mode((630,517))
pygame.display.set_caption("Ejercicio 1")
fondo = pygame.image.load("fondo.png")

fondorect = fondo.get_rect()
ventana.blit(fondo,[2,2])

brick = pygame.image.load("brick.png")
brickrect = brick.get_rect()
brickrect.move_ip(5, 5)


listblrick = []
for file in range(filas):
    bloque_filas = []
    for columna in range (columnas):
        




jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    ventana.blit(fondo, fondorect)
    ventana.blit(brick, brickrect)
    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()


