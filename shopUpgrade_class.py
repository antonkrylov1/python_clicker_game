import pygame
from settings import *

class ShopUpgrade:
    def __init__(self, num):
        self.num = num
        self.image = pygame.image.load(f"assets/upgrade{num + 1}.png") #Подгрузка изображений улучшений в магазине
        self.image = pygame.transform.scale(self.image, (65, 65)) #Установка размера изображений улучшений

        if num == 0:
            self.x = 125
            self.cost = 50
            self.product = 5

        if num == 1:
            self.x = WIDTH // 2
            self.cost = 100
            self.product = 10

        if num == 2:
            self.x = WIDTH // 2 + 125
            self.cost = 200
            self.product = 20

        self.y = HEIGHT // 2 + 50
        self.rect = pygame.Rect(self.x - self.image.get_width() // 2, self.y - self.image.get_height() // 2, 65, 65)
    
    def draw(self, screen):
        screen.blit(self.image, (self.x - self.image.get_size()[0] // 2, self.y - self.image.get_size()[1] // 2))
    
    def touching_mouse_pointer(self):
        mouse = pygame.Rect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 12, 17)
        return bool(self.rect.colliderect(mouse))