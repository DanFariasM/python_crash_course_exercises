class Settings:
    """A class to store all settings for the rocket game."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (100, 255, 255)

        # Rocket settings.
        self.rocket_speed = 1.5
