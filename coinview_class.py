import pygame

from settings import *
from coinViewUpgrade_class import *

class CoinView:
    def __init__(self):

        self.image = pygame.image.load("assets/coinup.png") #Подгрузка изображения магазина
        self.image = pygame.transform.scale(self.image, (425, 300)) #Установка размера изображения магазина

        # Размещение изображения магазина по центру окна
        self.x = WIDTH // 2
        self.y = HEIGHT // 2

        self.upgrades = [] #Улучшения в магазине



