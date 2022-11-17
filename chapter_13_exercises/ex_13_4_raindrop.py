import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """A class to represent a single raindrop in the rain."""

    def __init__(self, ai_game):
        """Initialize the raindrop and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the raindrop image and set its rect attribute.
        self.image = pygame.image.load("images/raindrop.jpg")
        self.rect = self.image.get_rect()

        # Start each new raindrop near the top left of the screen.
        self.rect.y = self.rect.height


    def check_edges(self):
        """Return True if an raindrop is at the edge of the screen."""
        screen_rect = self.screen.get_rect()

        if self.rect.top >= screen_rect.bottom:
            return True