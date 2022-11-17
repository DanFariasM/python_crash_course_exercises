import sys
import pygame

from ex_13_3_settings import Settings
from ex_13_3_raindrop import Raindrop

class RaindropRain:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Raindrops")

        self.raindrops = pygame.sprite.Group()

        self._create_rain()

    def _check_events(self):
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        # Respond to key presses.
        if event.key == pygame.K_q:
            sys.exit()

    def _create_rain(self):
        """Create the rain of raindrops."""
        # Make an raindrop and find the number of raindrops in a row.
        # Spacing between each raindrop is equal to one raindrop width.
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        available_space_x = self.settings.screen_width
        number_raindrops_x = available_space_x // (2 * raindrop_width)

        # Determine the number of rows of raindrops that fit on the screen.
        available_space_y = self.settings.screen_height
        number_rows = available_space_y // (2 * raindrop_height)

        # Create the full rain of raindrops.
        for row_number in range(number_rows):
            for raindrop_number in range(number_raindrops_x):
                self._create_raindrop(raindrop_number, row_number)

    def _create_raindrop(self, raindrop_number, row_number):
        """Create a raindrop and place it in the row."""
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        raindrop.x = raindrop_width + 2 * raindrop_width * raindrop_number
        raindrop.rect.x = raindrop.x
        raindrop.rect.y = raindrop_height + 2 * raindrop_height * row_number
        self.raindrops.add(raindrop)

    def _make_rain(self):
        """Respond appropriately if any raindrops have reached an edge."""
        for raindrop in self.raindrops.sprites():
            raindrop.rect.y += self.settings.rain_drop_speed

    def _update_raindrops(self):
        """Check if the rain is at an edge,
        then update the positions of all raindrops in the rain.
        """
        self._make_rain()
        self.raindrops.update()

    def _update_screen(self):
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_raindrops()
            self._update_screen()

if __name__ == "__main__":
    # Make a game instance and run the game.
    rd = RaindropRain()
    rd.run_game()
