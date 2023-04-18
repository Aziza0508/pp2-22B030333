'''

import pygame

pygame.init()
size = [600, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Feeling it in my balls, man")

radius = 25
clock = pygame.time.Clock()
velocity = 20
x, y = 100, 100
screenWidth, screenHeight = size

running = True

while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - 25 > 0:
        x -= velocity
    if keys[pygame.K_RIGHT] and x + 25 < screenWidth:
        x += velocity
    if keys[pygame.K_UP] and y - 25 > 0:
        y -= velocity
    if keys[pygame.K_DOWN] and y + 25 < screenHeight:
        y += velocity

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)

    pygame.display.flip()

pygame.quit()
'''