import pygame 
from pygame.sprite import Sprite
class Ship(Sprite):
    '''Класс для управления кораблём.'''
    def __init__(self, ai_game):
        '''Инициализирует корабль и задаёт его начальную позицию.'''
        super().__init__()
        self.screen = ai_game.screen 
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохранение вещественной координаты центра корабля.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Флаги перемещения
        self.moving_right = False
        self.moving_left = False 
        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''Обновляет позицию кораблся с учётом флага.'''
        # Обноволяется атрибут x, не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed_factor
        
        # Обновление атрибута rect на основании self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        '''Рисует корабль в текущей позиции.'''
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        '''Размещает корабль в центре нижней стороны.'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
