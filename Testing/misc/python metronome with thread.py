import pygame
import threading
import time

# Metronome parameters
bpm = 120  # Beats per minute
beat_sound_path = "metronomee.wav"  # Path to your metronome sound file
beat_interval = 60.0 / bpm  # Calculate the time interval between beats

# Initialize Pygame
pygame.init()

# Create a window for visualization
window_size = (400, 200)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Metronome")

# Load the metronome sound
metronome_sound = pygame.mixer.Sound(beat_sound_path)

# Function to play the metronome sound
def play_metronome_sound():
    while True:
        metronome_sound.play()
        time.sleep(beat_interval)

# Create a thread for the metronome sound
metronome_thread = threading.Thread(target=play_metronome_sound)
metronome_thread.daemon = True  # Allow the thread to exit when the program exits

# Start the metronome thread
metronome_thread.start()

# Main loop for visualization
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw a visual metronome beat
    pygame.draw.circle(screen, (255, 0, 0), (200, 100), 30)
    pygame.display.flip()

    # Wait for the beat interval
    time.sleep(beat_interval)
    screen.fill((0, 0, 0))  # Clear the visualization

put = input()
print(put)


# Clean up
pygame.quit()
