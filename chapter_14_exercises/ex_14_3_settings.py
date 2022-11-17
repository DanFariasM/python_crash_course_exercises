class Settings:
    """A class to store all settings for Target Practice."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings.
        self.ship_limit = 2

        # Bullet settings
        self.bullet_width = 15
        self.bullet_height = 300
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up.
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5        
        self.bullet_speed = 1.0
        self.alien_speed = 1.0

        # Fleet direction of 1 represents down, -1 represents up.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase alien speed."""
        self.alien_speed *= self.speedup_scale