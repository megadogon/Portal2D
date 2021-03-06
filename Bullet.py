import pygame

import Helper
import math


# класс - пуля
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.red_image = Helper.load_image('red_bullet.png')
        self.blue_image = Helper.load_image('blue_bullet.png')
        self.image = self.blue_image
        self.rect = self.blue_image.get_rect()
        self.visible = False
        self.red = True

        # создаем группу спрайтов и добавляем в нее пулю
        self.group = pygame.sprite.Group()
        self.group.add(self)

        # звук выстрела
        self.sound = pygame.mixer.Sound('data/purr.wav')

        # маска для подсчета столкновений
        self.mask = pygame.mask.from_surface(self.image)

    # запуск пули
    def start(self, x1, y1, x2, y2):
        if self.red:
            self.image = self.red_image
        else:
            self.image = self.blue_image
        self.x1 = x1 - self.image.get_width() // 2
        self.y1 = y1 - self.image.get_height() // 2
        self.x2 = x2
        self.y2 = y2
        self.x = self.x1
        self.y = self.y1
        self.visible = True
        self.sound.play()

    # перемещение пули на 1 пиксель
    def move(self):
        # длина всего пути
        d = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        # на сколько перещещаем пулю по X и Y
        dx = (self.x2 - self.x1) / d
        dy = (self.y2 - self.y1) / d
        self.x += dx
        self.y += dy
        # округляем координаты для рисования спрайта
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    # рисование пули на экране
    def draw(self, screen):
        self.group.draw(screen)
