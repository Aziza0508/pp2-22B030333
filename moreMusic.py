'''
import pygame
import os

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((640, 480))

# Define the keyboard keys for controlling the music
play_key = pygame.K_UP
stop_key = pygame.K_SPACE
next_key = pygame.K_RIGHT
prev_key = pygame.K_LEFT

# Define the folder where the music files are located
music_folder = "musics"

# Get a list of all music files in the folder
music_files = [os.path.join(music_folder, f) for f in os.listdir(music_folder) if f.endswith(".mp3")]

# Start playing the first music file in the list
current_track = 0
pygame.mixer.music.load(music_files[current_track])
pygame.mixer.music.play()

# Main loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            # Handle keyboard events
            if event.key == play_key:
                pygame.mixer.music.unpause()
            elif event.key == stop_key:
                pygame.mixer.music.pause()
            elif event.key == next_key:
                current_track = (current_track + 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_track])
                pygame.mixer.music.play()
            elif event.key == prev_key:
                current_track = (current_track - 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_track])
                pygame.mixer.music.play()
    
    # Update the screen
    pygame.display.update()
'''