class Settings():
    '''Класс для хранения всех настроек игры Alien Invasion.'''

    def __init__(self):
        '''Инициализирует настройки игры.'''
        # Параметры экрана
        self.screen_width = 1080
        self.screen_height = 960
        self.bg_color = (230, 230, 230)

        # Настройка корабля 
        self.ship_speed = 2
        self.ship_limit = 3 

        # Параметры снаряда 
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_hight = 15 
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        # Настройка пришельцев.
        self.alien_speed = 0.5
        self.fleet_drop_speed = 5
        # fleet_direction = 1 обозначает движение вправо; a -1 - влево.
        self.fleet_direction = 1 


