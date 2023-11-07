import pygame

pygame.init()
pygame.mixer.init()
audio = pygame.mixer.Sound('../piano_testing_and_files/V3_programming_project/PianoC.wav')  # Load your audio file
audio.play()  # Start playing the audio
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Your game logic and rendering here

# Quit Pygame when the game is done
pygame.quit()
