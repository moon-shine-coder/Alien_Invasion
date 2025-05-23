class Settings():
    '''Класс для хранения всех настроек игры Alien Invasion.'''

    def __init__(self):
        '''Инициализирует статические настройки игры.'''
        # Параметры экрана
        self.screen_width = 1080
        self.screen_height = 960
        self.bg_color = (230, 230, 230)

        # Настройка корабля 
        self.ship_limit = 2

        # Параметры снаряда 
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_hight = 15 
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        # Настройка пришельцев.
        self.fleet_drop_speed = 3

        # Темп ускорения игры.
        self.speedup_scale = 1.1

        # Темп роста стоимости пришельцев.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        '''Инициализирует настройки, изменяющиеся во время игры.'''
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0

        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1 

        # Подсчёт очков.
        self.alien_points = 50
    
    def increase_speed(self):
        '''Увеличивает настройки скорости и стоимость пришельцев.'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)