'''
import pygame
import time
import math

pygame.init()

size = (800, 800)
screen = pygame.display.set_mode(size)

background_image = pygame.image.load("clock.png")
screen.blit(background_image, (0, 0))

mickey_image = pygame.image.load("clock.png")
mickey_rect = mickey_image.get_rect()
mickey_rect.center = (400, 400)


seconds_image = pygame.image.load("long.png")
seconds_rect = seconds_image.get_rect()
seconds_rect.bottomright = background_image.get_rect().center


minutes_image = pygame.image.load("short.png")
minutes_rect = minutes_image.get_rect(center=mickey_rect.center)

def rotate_hands():
    # Get the current time in seconds and minutes
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min

    # Calculate the angle for the second hand and rotate it
    seconds_angle = math.radians(6 * seconds - 90)
    seconds_hand = pygame.transform.rotate(seconds_image, math.degrees(seconds_angle))

    # Calculate the angle for the minute hand and rotate it
    minutes_angle = math.radians(6 * minutes - 90)
    minutes_hand = pygame.transform.rotate(minutes_image, math.degrees(minutes_angle))

    # Draw the hands on the screen
    screen.blit(minutes_hand, minutes_rect)
    screen.blit(seconds_hand, seconds_rect)


running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background and Mickey Mouse's image
    screen.blit(background_image, (0, 0))
    screen.blit(mickey_image, mickey_rect)

    # Rotate the hands
    rotate_hands()

    # Update the display
    pygame.display.update()

    # Wait for 1 second
    time.sleep(1)

# Quit Pygame
pygame.quit()
'''