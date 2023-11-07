import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font(None, 36)  # None means use the default font, 36 is the font size

def render_text(text, x, y):
    text_surface = font.render(text, True, (255, 255, 255))  # Text, antialiasing, color
    screen.blit(text_surface, (x, y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill((0, 0, 0))  # Clear the screen

    # Render multiple text elements
    render_text("Hello, Pygame!", 100, 100)
    render_text("This is another text element", 100, 200)
    render_text("You can render as many as you need", 100, 300)

    pygame.display.flip()  # Update the display

pygame.quit()
