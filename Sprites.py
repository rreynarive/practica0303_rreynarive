import pygame

class Ball():
    def __init__(self,velocidad, image_ruta):
        self.__image = pygame.image.load(image_ruta)
        self.__rect = self.__image.get_rect()
        self.__rect.move_ip(310, 450)
        self.__velocidad = velocidad
        self.movx = 1
        self.movy = -1

    @property
    def image(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect
    @rect.setter
    def rect(self, valor):
        self.__rect = valor

#velocidad
    @property
    def speed(self):
        return self.__velocidad

    @speed.setter
    def speed(self, valor):
        self.__velocidad = valor

#Movimiento
    @property
    def movx(self):
        return self.__movx

    @movx.setter
    def movx(self, valor):
        self.__movx = valor

    @property
    def movy(self):
        return self.__movy

    @movy.setter
    def movy(self, valor):
        self.__movy = valor



class Barra():
    def __init__(self, velocidad, image_ruta):
        self.__image = pygame.image.load(image_ruta)
        self.__rect = self.__image.get_rect()
        self.__rect.move_ip(280, 480)
        self.__velocidad = velocidad
        self.__prev_dir = -1

    @property
    def image(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, valor):
        self.__rect = valor

    @property
    def velocidad(self):
        return self.__velocidad
    @velocidad.setter
    def velocidad(self, valor):
        self.__velocidad = valor
    @property
    def prev_dir(self):
        return self.__prev_dir

    @prev_dir.setter
    def prev_dir(self, valor):
        self.__prev_dir = valor



class Brick():
    def __init__(self, pos_x, pos_y, image_ruta):
        self.__image = pygame.image.load(image_ruta)
        self.__rect = self.image.get_rect()
        self.__rect.move_ip(pos_x, pos_y)

    @property
    def rect(self):
        return self.__rect

    @property
    def image(self):
        return self.__image

    def move(self, posi_x, posi_y):
        self.__rect.move(posi_x, posi_y)
