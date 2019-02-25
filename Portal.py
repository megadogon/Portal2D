import pygame

import Helper


class Portal(pygame.sprite.Sprite):
    TOP = 0
    BOTTOM = 1
    LEFT = 2
    RIGHT = 3

    def __init__(self, vert_image, horz_image):
        super().__init__()

        self.vert_image = Helper.load_image(vert_image)
        self.horz_image = Helper.load_image(horz_image)

        self.visible = False

        self.group = pygame.sprite.Group()
        self.group.add(self)

    def top(self, rect):
        self.image = self.horz_image
        self.rect = self.horz_image.get_rect()
        self.rect.x = rect.x
        self.rect.y = rect.y - 2
        self.visible = True
        self.orientation = Portal.TOP

    def bottom(self, rect):
        self.image = self.horz_image
        self.rect = self.horz_image.get_rect()
        self.rect.x = rect.x
        self.rect.y = rect.y + rect.h - 2
        self.visible = True
        self.orientation = Portal.BOTTOM

    def left(self, rect):
        self.image = self.vert_image
        self.rect = self.vert_image.get_rect()
        self.rect.x = rect.x - 2
        self.rect.y = rect.y
        self.visible = True
        self.orientation = Portal.LEFT

    def right(self, rect):
        self.image = self.vert_image
        self.rect = self.vert_image.get_rect()
        self.rect.x = rect.x + rect.w - 2
        self.rect.y = rect.y
        self.visible = True
        self.orientation = Portal.RIGHT

    def teleport(self, human):
        if self.orientation == Portal.TOP:
            human.rect.x = self.rect.x
            human.rect.y = self.rect.y - human.rect.h
        elif self.orientation == Portal.BOTTOM:
            human.rect.x = self.rect.x
            human.rect.y = self.rect.y + self.rect.h
        elif self.orientation == Portal.LEFT:
            human.rect.x = self.rect.x - human.rect.w
            human.rect.y = self.rect.y
        elif self.orientation == Portal.RIGHT:
            human.rect.x = self.rect.x + self.rect.w
            human.rect.y = self.rect.y

    def draw(self, screen):
        self.group.draw(screen)
