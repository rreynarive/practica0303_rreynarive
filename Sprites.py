import pygame

class Ball():
    def __init__(self, image_ruta):
        self.__image = pygame.image.load(image_ruta)
        self.__rect = self.__image.get_rect()
        self.__rect.move_ip(310, 450)

    @property
    def image(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect


class Barra():
    def __init__(self, image_ruta):
        self.__image = pygame.image.load(image_ruta)
        self.__rect = self.__image.get_rect()
        self.__rect.move_ip(280, 480)

    @property
    def image(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect


class Brick():
    def __init__(self, x, y, image_ruta):
        self.__image = pygame.image.load(image_ruta)
        self.__rect = self.image.get_rect()
        self.__rect.move_ip(x, y)

    @property
    def rect(self):
        return self.__rect

    @property
    def image(self):
        return self.__image

    def move(self, posix, posiy):
        self.__rect.move(posix, posiy)