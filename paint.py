import pygame

pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE =(0, 255, 0)
GREEN =(0, 0, 255)

FPS = 60

WIDTH, HEIGHT = 500, 600

ROWS = COLS = 50

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH // COLS

BG_COLOR = WHITE

DRAW_GRID_LINES = True

def get_font(size):
    return pygame.font.SysFont("comicsans", size)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

def init_grid(rows, cols, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)

    return grid

def draw_grid(window, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(window, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(window, BLACK, (0, i * PIXEL_SIZE), (WIDTH, i * PIXEL_SIZE))

        
        for i in range(COLS + 1):
            pygame.draw.line(window, BLACK, (i * PIXEL_SIZE, 0), (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))

def draw(window, grid, buttons):
    window.fill(BG_COLOR)
    draw_grid(window, grid)
    pygame.display.update()

    for button in buttons:
        button.draw(window)


def get_rc_pos(pos):

    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError

    return row, col

run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK


class Button:
    def __init__(self, x, y, width, height, color, text=None, text_color =BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(window, BLACK, (self.x, self.y, self.width, self.height), 2)

        if self.text:
            button_font = get_font(22)
            text_surface = button_font.render(self.text, 1, self.text_color)
            window.blit(text_surface, (self.x + self.width/2 - text_surface.get_width()/2, self.y + self.height/2 - text_surface.get_height()/2))
        


    def clicked(self, pos):
        x, y = pos
        if not (x >= self.x and x <= self.x + self.width):
            return False
        if not (y >= self.y and y <= self.x + self.height):
            return False
        
        return True

button_y = HEIGHT - TOOLBAR_HEIGHT/2 - 25
buttons = [
    Button (10, button_y, 50, 50, BLACK),
    Button (70, button_y, 50, 50, RED),
    Button (130, button_y, 50, 50, GREEN),
    Button (190, button_y, 50, 50, BLUE),
    Button (250, button_y, 50, 50, WHITE, "Erase", BLACK),
    Button (310, button_y, 50, 50, WHITE, "Clear", BLACK)

]

while run:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

            try:
                row, col = get_rc_pos(pos)
                grid[row][col] = drawing_color
            except IndexError:
                pass

    

    draw(WIN, grid, buttons)

pygame.quit()