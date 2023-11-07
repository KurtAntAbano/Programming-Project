import threading
import time

import pygame


white = (255, 255, 255)
# Initialize Pygame
pygame.init()

# Constants
BPM = 120  # Beats per minute
INTERVAL = 60.0 / BPM  # Calculate the time interval in seconds

# Initialize the audio mixer
pygame.mixer.init()

# Load your metronome sound file
metronome_sound = pygame.mixer.Sound("metronome.wav")  # Replace with your sound file


def play_metronome():
    while True:
        # pygame.event.post(pygame.event.Event(pygame.USEREVENT, {}))  # Post a custom event
        metronome_sound.play()
        time.sleep(INTERVAL)

#
# font = pygame.font.Font(None, 36)  # None means use the default font, 36 is the font size
#
#
# def render_text(text, x, y):
#     text_surface = font.render(text, True, (255, 255, 255))  # Text, antialiasing, color
#     screen.blit(text_surface, (x, y))

def metromain():
    # Create a thread for the metronome
    metronome_thread = threading.Thread(target=play_metronome)

    # Start the metronome thread
    metronome_thread.start()

    # Set up Pygame
    screen = pygame.display.set_mode((400, 150))
    pygame.display.set_caption("Metronome Example")

    running = True
    # clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    running = False
            elif event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.USEREVENT:  # Custom event
                print("Beat!")

        screen.fill((0, 0, 0))  # Clear the screen

        # render_text("Metranome now playing!", 50, 50)  # Rendering multiple text
        # render_text("Press 's' to stop", 50, 100)

        # Update the display
        pygame.display.flip()

    pygame.quit()

metromain()