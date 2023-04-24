import pygame, sys, random, datetime

from pygame.math import Vector2


class Constants:
    UP = Vector2(0, -1)
    DOWN = Vector2(0, 1)
    LEFT = Vector2(-1, 0)
    RIGHT = Vector2(1, 0)
    fruits = {1: "apple", 2: "banana", 3: "strawberry"}

class FRUIT :
    def __init__(self):
        self.weight = 1
        self.position = Vector2(random.randint(1, cell_number - 3), random.randint(1, cell_number - 3))
        self.image = pygame.transform.scale(pygame.image.load(f"{Constants.fruits[self.weight]}.png").convert_alpha(),
                                            (cell_size, cell_size))
        self.timestamp = datetime.datetime.now()

    def setTimer(self):
        now = datetime.datetime.now()
        if (now - self.timestamp).seconds.real >= 3:
            self.move()

    # def draw_fruit(self):
    #     fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
    #     screen.blit(apple, fruit_rect)
    #     # pygame.draw.rect(screen, (126, 166, 114), fruit_rect)

    def draw_fruit(self):
        self.setTimer()
        rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size)
        screen.blit(self.image, rect)

    def move(self):
        self.position = Vector2(random.randint(1, cell_number - 2), random.randint(1, cell_number - 2))
        self.weight = random.randint(1, 3)
        self.image = pygame.transform.scale(pygame.image.load(f"{Constants.fruits[self.weight]}.png").convert_alpha(),
                                            (cell_size, cell_size))
        self.timestamp = datetime.datetime.now()

    def get_pos(self) -> tuple[float, float]:
        return self.position.x, self.position.y

    # def randomize(self) :
    #     self.x = random.randint(0, cell_number - 1)
    #     self.y = random.randint(0, cell_number - 1)
    #     self.pos = Vector2(self.x, self.y)


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)

            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (183, 111, 122), block_rect)

    def move_snake(self):

        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

        

    def add_block(self):
        self.new_block = True

    def get_pos(self) -> tuple[float, float]:
        return self.body[0].x, self.body[0].y

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)

class PlayBoard:
    def __init__(self, ):
        self.cell_number = cell_number
        self.cell_size = cell_size
    

class MAIN:
    def __init__ (self, playb: PlayBoard):
        self.playb = playb
        self.font = pygame.font.SysFont("Arial", 16)
        self.score_text = 0
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.TICK = 125
        self.currLevel = 1
        self.SIZE = (playb.cell_number * playb.cell_size, playb.cell_number * playb.cell_size)
        self.screen = pygame.display.set_mode(self.SIZE)

    def renderGameInfo(self):
        level = self.font.render(f"Level {self.currLevel}", True, (0, 0, 0))
        # score = self.font.render(f"Score {self.score_text}", True, (0, 0, 0))
        self.screen.blit(level, ((self.playb.cell_number - 2) * self.playb.cell_size, 20.0))
        # self.screen.blit(score, ((self.playb.cell_number - 2) * self.playb.cell_size, 40.0))

    # def increaseLevel(self):
    #     self.currLevel += 1
    #     if self.TICK > 40:
    #         self.TICK -= 20

    def checkForCollision(self):
        
        # self.score_text = str(len(self.snake.body) - 3)

        # if self.score_text % 3 == 0:
        #     self.increaseLevel()
        #     pygame.time.set_timer(MOVEMENT, self.TICK)

        headC = self.snake.get_pos()
        appleC = self.fruit.get_pos()
        if appleC == headC:
            self.fruit.move()
            self.snake.move_snake()
            self.score_text += self.fruit.weight

        self.currLevel = str(int((len(self.snake.body)-3) / 4))

    def update(self):
        self.snake.move_snake()
        self.ckeck_coliision()
        self.check_fail()
        self.renderGameInfo()
        self.checkForCollision()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
        self.draw_level()
        

    def ckeck_coliision (self):
        if self.fruit.position == self.snake.body[0]:
            self.fruit.move()
            self.snake.add_block()

        for block in self.snake.body[1:]:
            if block == self.fruit.position:
                self.fruit.move()

    def check_fail(self):
        # outside of screen
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        # hit itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        # pygame.quit()
        # sys.exit()
        self.snake.reset()

    def draw_grass(self):
        grass_color = (167, 209, 61)

        for row in range(cell_number):
            if row % 2 == 0:
                for col in range (cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range (cell_number):
                    if col % 2 == 1:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))
        
        
        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)

    def draw_level(self):
        level_text = str(self.currLevel)
        level_surface = game_font.render(level_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 90)
        level_rect = level_surface.get_rect(center = (score_x, score_y))
        level_pic_rect = level.get_rect(midright = (level_rect.left, level_rect.centery))
        
        
        screen.blit(level_surface, level_rect)
        screen.blit(level, level_pic_rect)

pygame.init()

cell_size = 40
cell_number = 15

screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
clock = pygame.time.Clock()

apple = pygame.image.load('apple.png').convert_alpha()
game_font = pygame.font.Font(None, 25)
level = pygame.image.load("level.png").convert_alpha()


# fruit = FRUIT()
# snake = SNAKE()
main_game = MAIN(PlayBoard())

SCREEN_UPDATE = pygame.USEREVENT #we do not wanna change
pygame.time.set_timer(SCREEN_UPDATE, 150) 




while 1:

    speed_dependence = int(main_game.currLevel) + 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -(1))
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, (1))
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2((1), 0)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-(1), 0)
    

    screen.fill((175, 215, 70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)

    