class Settings():
    '''Класс для хранения всех настроек игры Alien Invasion.'''

    def __init__(self):
        '''Инициализирует настройки игры.'''
        # Параметры экрана
        self.screen_width = 1080
        self.screen_height = 960
        self.bg_color = (230, 230, 230)

        # Настройка корабля 
        self.ship_speed = 1.5