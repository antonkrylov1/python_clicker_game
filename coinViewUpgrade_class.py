import pygame
from settings import *
from coin_class import *

class CoinViewUpgrade:
    def __init__(self):
        self.name = 'Биткоин'
        self.image1 = pygame.image.load(f"assets/coin1.png")  ##Подгрузка изображений улучшений в магазине
        self.image1 = pygame.transform.scale(self.image1, (85, 85))
        self.image2 = pygame.image.load(f"assets/coin2.png")
        self.image2 = pygame.transform.scale(self.image2, (85, 85))
        self.image3 = pygame.image.load(f"assets/coin3.png")  ##Подгрузка изображений улучшений в магазине
        self.image3 = pygame.transform.scale(self.image3, (85, 85))

        self.y = HEIGHT // 2 + 10

        self.rect1 = pygame.Rect(125 - self.image1.get_width() // 2, self.y - self.image1.get_height() // 2, 85, 85)
        self.rect2 = pygame.Rect(WIDTH // 2 - self.image2.get_width() // 2, self.y - self.image2.get_height() // 2, 85, 85)
        self.rect3 = pygame.Rect(WIDTH // 2 + 125 - self.image3.get_width() // 2, self.y - self.image3.get_height() // 2, 85, 85)

    def draw(self, screen):
        self.coin_1 = screen.blit(self.image1, (125 - self.image1.get_size()[0] // 2, self.y - self.image1.get_size()[1] // 2))
        self.coin_2 = screen.blit(self.image2, (WIDTH // 2 - self.image1.get_size()[0] // 2, self.y - self.image2.get_size()[1] // 2))
        self.coin_3 = screen.blit(self.image3, (WIDTH // 2 + 125 - self.image3.get_size()[0] // 2, self.y - self.image3.get_size()[1] // 2))

    def touching_mouse_pointer(self):
        mouse = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        if mouse[0] and self.coin_1.collidepoint(mouse_pos):
            self.name = 'Биткоин'
        elif mouse[0] and self.coin_2.collidepoint(mouse_pos):
            self.name = 'Рубль'
        elif mouse[0] and self.coin_3.collidepoint(mouse_pos):
            self.name = 'Доллар'