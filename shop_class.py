import pygame

from settings import *
from shopUpgrade_class import *

class Shop:
    def __init__(self):
        self.image = pygame.image.load("assets/shop.png") #Подгрузка изображения магазина
        self.image = pygame.transform.scale(self.image, (425, 300)) #Установка размера изображения магазина

        # Размещение изображения магазина по центру окна
        self.x = WIDTH // 2
        self.y = HEIGHT // 2

        self.upgrades = [] #Улучшения в магазине

        # 3 уровня улучшений в магазине
        for i in range(3):
            self.upgrades.append(ShopUpgrade(i))