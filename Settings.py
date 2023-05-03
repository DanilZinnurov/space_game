class settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed = 1.5
        self.ship_limit = 2
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
        self.alien_speed = 10.0
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо, -1 влево
        self.fleet_direction = 1