import pygame

class Bonfire:
    """a class to manage the ship."""

    def __init__(self, ds_game):
        """Initialize the ship and set its starting position."""
        self.screen = ds_game.screen
        self.screen_rect = ds_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load("images/bonfire.png")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

