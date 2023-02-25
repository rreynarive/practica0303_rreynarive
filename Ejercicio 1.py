import pygame

#Creacion de ventana de videojuego
pygame.init()

ventana = pygame.display.set_mode((630,517))
pygame.display.set_caption("Ejercicio 1")
fondo = pygame.image.load("fondo.png")

fondorect = fondo.get_rect()
ventana.blit(fondo,[2,2])


class ladrillos():
    def __init__(self):
        self.largo = 630 // columnas
        self.ancho = 50

    def ladrillo(self):
        self.listaladrillos = []
        for file in range(filas):
            bloque_filas = []
            for columna in range (columnas):
                bloque_x = columna * self.largo
                bloque_y = fila * self.ancho
                brick = pygame.image.load("brick.png")
                brickrect = brick.get_rect()
                rect = pygame.rect(bloque_x, bloque_y, self.largo, self.ancho)
                if fila < 2:
                    largo = 3
                elif columna < 4:
                    largo = 2
                elif fila < 6:
                    largo = 1
                # create a list at this point to store the rect and colour data
                block_individual = [rect, largo]
                # append that individual block to the block row
                bloque_filas.append(block_individual)
            # append the row to the full list of blocks
            self.listaladrillos.append(bloque_filas)
    def bloque(self):
        for fila in self.listaladrillos:
            for bloque in fila:
                pygame.draw.rect(ventana, bloque[0])
                pygame.draw.rect(ventana, bloque[0], 2)


ladrillos = ladrillos()
ladrillos.ladrillo()

jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    ladrillos.bloque()

    ventana.blit(fondo, fondorect)
    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()


