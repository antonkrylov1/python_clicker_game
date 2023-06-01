import math
import pygame
from pygame import mixer
from settings import *
from coin_class import *
from shop_class import *
from coinview_class import *
from coinViewUpgrade_class import *

class App:
    def __init__(self):
        pygame.init() #Инициализация pygame
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) #Доступ к отображению дисплея, передача размеров окна
        pygame.display.set_icon(pygame.image.load("assets/icon.ico")) #Подгрузка значка кликера монет
        pygame.display.set_caption("Clicker") #Отображение названия игры
        self.coin = Coin() #Инициализация класса монеты из coin_class
        self.money = 0 #Начальное значение кол-во монет
        self.state = "START"
        self.shop = Shop() #Инициализация класса магазина
        self.coinview = CoinView()
        self.click_value = 1 #Начальное значение кол-во кликов
        self.running = True #Для проверки игры на запуск
        self.coinViewUpgrade = CoinViewUpgrade()
        pygame.mixer.music.load("assets/sound.mp3")

    def write_text(self, words, size, pos, color, centered = False):
        font = pygame.font.SysFont(GAME_FONT, size)
        text = font.render(words, False, color)

        if centered: #Центрирование текста
            pos[0] = pos[0] - text.get_size()[0] // 2
            pos[1] = pos[1] - text.get_size()[1] // 2
        
        self.screen.blit(text, pos) #Накладывание текста и позиции на дисплей
    
    def start_events(self): #Проверка запуска игры
        for event in pygame.event.get():

            # Отслеживание события: "закрыть окно"
            if event.type == pygame.QUIT:
                self.running = False

            #Проверка на нажатие пробела для запуска игры
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.state = "PLAYING"
    
    def start_draw(self):
        self.write_text("Нажмите ПРОБЕЛ для запуска игры", 35, [WIDTH // 2, HEIGHT // 2], (255, 189, 8), centered = True)
    
    def playing_events(self):
        #Получаем события из очереди
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # При нажатии на монету прибавляем значение очков
            if event.type == pygame.MOUSEBUTTONDOWN:

                if self.get_distance((WIDTH // 2, HEIGHT // 2), (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])) <= self.coin.image.get_size()[0] // 2: #Проверка на нажатие ИМЕННО на монету, для прибавления монет
                    self.money += self.click_value
                    pygame.mixer.music.play(1)

            # Проверка на нажатие "S" для запуска внутриигрового магазина
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.state = "SHOP"
            # Проверка на нажатие "X" для изменения монеты
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_x:
                    self.state = "COIN"
    
    def playing_draw(self):

        self.write_text(f"Монеты: {self.money}", 30, [5, 0], RED) #Размещение счётчика кол-во монет в окне
        self.write_text("Нажмите 'X' для смены монеты", 30, [5, HEIGHT - 50], CYAN)  # Размещение текста о магазине
        self.write_text("Нажмите 'S' для открытия магазина",30, [5, HEIGHT - 25], CYAN) #Размещение текста о магазине
        self.write_text(f"Цена клика: {self.click_value}", 30, [WIDTH // 2, 5], (255, 255, 255)) #Размещение счётчика цены за клик
        self.screen.blit(self.coin.image, (self.coin.x - self.coin.image.get_size()[0] // 2, self.coin.y - self.coin.image.get_size()[1] // 2))
    
    def shop_events(self):
        # Получаем события из очереди
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.state = "PLAYING"
            
            for upgrade in self.shop.upgrades:
                if upgrade.touching_mouse_pointer():
                    self.write_text(f"Цена: {upgrade.cost}", 16, [WIDTH // 2, HEIGHT // 2 + 120], BLACK, centered = True)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.money >= upgrade.cost:
                            self.money -= upgrade.cost #Отнимает из кол-во монет цену улучшения
                            self.click_value += upgrade.product #Прибавляем цену клика при покупке улучшения

    def coin_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    self.state = "PLAYING"

    def coinView_draw(self):
        self.write_text(f"Монеты: {self.money}", 30, [5, 0], RED)
        self.write_text("Нажмите 'X' для выхода", 30, [5, HEIGHT - 25], CYAN)
        self.write_text(f"Цена клика: {self.click_value}", 30, [WIDTH // 2, 5], (255, 255, 255))
        self.screen.blit(self.coinview.image, (self.coinview.x - self.coinview.image.get_size()[0] // 2, self.coinview.y - self.coinview.image.get_size()[1] // 2))

        for i in self.coinview.upgrades:
            i.draw(self.screen)
    def shop_draw(self):

        self.write_text(f"Монеты: {self.money}", 30, [5, 0], RED)
        self.write_text("Нажмите 'S' для закрытия магазина", 30, [5, HEIGHT - 25], CYAN)
        self.write_text(f"Цена клика: {self.click_value}", 30, [WIDTH // 2, 5], (255, 255, 255))
        self.screen.blit(self.shop.image, (self.shop.x - self.shop.image.get_size()[0] // 2, self.shop.y - self.shop.image.get_size()[1] // 2))

        for i in self.shop.upgrades:
            i.draw(self.screen)

    # Прибавление очков только при нажатии ИМЕННО на монету
    def get_distance(self, pos_1, pos_2):
        return math.sqrt(((pos_2[0] - pos_1[0]) ** 2) + ((pos_2[1] - pos_1[1]) ** 2))
    
    def run(self):
        while self.running:
            self.screen.fill(BLACK) #Заливка окна чёрным цветом

            if self.state == "START":
                self.start_events()
                self.start_draw()
            
            if self.state == "PLAYING":
                self.playing_events()
                self.playing_draw()
            
            if self.state == "SHOP":
                self.shop_draw()
                self.shop_events()

            if self.state == "COIN":
                self.coin_events()
                self.coinView_draw()
                self.coinViewUpgrade.touching_mouse_pointer()
                self.coinViewUpgrade.draw(self.screen)
            if self.coinViewUpgrade.name == 'Биткоин':
                self.coin.image = pygame.image.load("assets/coin1.png")
                self.coin.image = pygame.transform.scale(self.coin.image, (150, 150))
            elif self.coinViewUpgrade.name == 'Рубль':
                self.coin.image = pygame.image.load("assets/coin2.png")
                self.coin.image = pygame.transform.scale(self.coin.image, (150, 150))
            else:
                self.coin.image = pygame.image.load("assets/coin3.png")
                self.coin.image = pygame.transform.scale(self.coin.image, (150, 150))

            pygame.display.update()