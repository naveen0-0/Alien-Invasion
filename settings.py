class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed=1.5
        self.ship_limit=3

        # Bullet Settings
        self.bullet_speed=1.5
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,230)
        self.bullets_allowed = 5

        #Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed=10
        self.fleet_direction=1