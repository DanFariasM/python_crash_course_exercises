import pygame
import sys

screen = pygame.display.set_mode((250, 250))
background = screen.fill((230, 230, 230))
pygame.display.flip()

while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event)
