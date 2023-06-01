import pygame

from settings import *
from coinViewUpgrade_class import *


class Coin:
    
    def __init__(self):

        self.image = pygame.image.load("assets/coin1.png") #Подгрузка изображения монеты
        self.image = pygame.transform.scale(self.image, (150, 150))#Установка размера изображения монеты

        #Размещение изображения монеты по центру окна
        self.x = WIDTH // 2
        self.y = HEIGHT // 2