'''
import pygame


pygame.init()

# Load the music file
music_file = "lullaby.mp3"
pygame.mixer.music.load(music_file)

screen = pygame.display.set_mode((640, 480))

play_key = pygame.K_UP
stop_key = pygame.K_SPACE
next_key = pygame.K_RIGHT
prev_key = pygame.K_LEFT

# Start playing the music
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
                pygame.mixer.music.stop()
                pygame.mixer.music.play()
            elif event.key == prev_key:
                pygame.mixer.music.stop()
                pygame.mixer.music.play(-1)
    
    # Update the screen
    pygame.display.update()
'''