import pygame
import sys
import random
from pygame.locals import *

# Initialize Pygame
pygame.init()
pygame.font.init()  # Initialize the font module

# Global Variables For The Game
FPS = 60
SCREENWIDTH = 900
SCREENHEIGHT = 900
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
FPSCLOCK = pygame.time.Clock()

# Game states
WELCOME_SCREEN = 0
FLAPPY_BIRD = 1
SNAKE_GAME = 2

# Game variables
current_game = WELCOME_SCREEN
change_game = False

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Fonts
font = pygame.font.Font(None, 36)

# Flappy Bird Variables
import random
import sys
import pygame
from pygame.locals import *
FPS = 32
SCREENWIDTH = 900
SCREENHEIGHT = 900
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'sprites/redbird-upflap.png'
BACKGROUND_DAY = 'sprites/background-day.png'
BACKGROUND_NIGHT = 'sprites/background-night.png'
PIPE = 'sprites/pipe-green.png'
CHANGE_BACKGROUND_INTERVAL = 12000  # Change background every 5 seconds
last_background_change_time = 0
bird_flap_positions = ['sprites/redbird-upflap.png', 'sprites/redbird-midflap.png', 'sprites/redbird-downflap.png']


# Snake Game Variables
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load('Graphics/apple.png').convert_alpha()
game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)

#welcome
background_image = pygame.image.load("sprites/ss.png").convert()
background_image = pygame.transform.scale(background_image, (800,900))

background_rect = background_image.get_rect()



SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

def welcome_screen():
    global current_game, change_game

    selected_game = 1  # Initial selection

    title_text = font.render(" ", True, WHITE)
    title_rect = title_text.get_rect(center=(SCREENWIDTH // 2, 100))

    flappy_bird_text = font.render(" ", True, WHITE)
    flappy_bird_rect = flappy_bird_text.get_rect(center=(SCREENWIDTH // 2, 300))

    snake_game_text = font.render(" ", True, WHITE)
    snake_game_rect = snake_game_text.get_rect(center=(SCREENWIDTH // 2, 500))

    screen_rect = SCREEN.get_rect()
    


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_UP:
                    selected_game = max(1, selected_game - 1)
                elif event.key == K_DOWN:
                    selected_game = min(2, selected_game + 1)
                elif event.key == K_RETURN:
                    current_game = selected_game
                    change_game = True
        
        SCREEN.blit(background_image, background_rect)
        SCREEN.blit(title_text, title_rect)
        SCREEN.blit(flappy_bird_text, flappy_bird_rect)
        SCREEN.blit(snake_game_text, snake_game_rect)

        # Draw selection indicator
        pygame.draw.rect(SCREEN, RED, (flappy_bird_rect.x - 230, flappy_bird_rect.y + 110 + selected_game * 175, 30, 30), 0)

        pygame.display.flip()
        FPSCLOCK.tick(FPS)

        if change_game:
            return


def flappy_bird_game():
     # Global Variables For The Game
    FPS = 32
    SCREENWIDTH = 289
    SCREENHEIGHT = 511
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    GROUNDY = SCREENHEIGHT * 0.8
    GAME_SPRITES = {}
    GAME_SOUNDS = {}
    PLAYER = 'sprites/redbird-upflap.png'
    BACKGROUND_DAY = 'sprites/background-day.png'
    BACKGROUND_NIGHT = 'sprites/background-night.png'
    PIPE = 'sprites/pipe-green.png'
    CHANGE_BACKGROUND_INTERVAL = 12000  # Change background every 5 seconds
    last_background_change_time = 0
    bird_flap_positions = ['sprites/redbird-upflap.png', 'sprites/redbird-midflap.png', 'sprites/redbird-downflap.png']

    def welcomeScreen():
        playerx = int(SCREENWIDTH / 5)
        playery = int(SCREENHEIGHT - GAME_SPRITES['player'].get_height()) / 2
        messsagex = int(SCREENWIDTH - GAME_SPRITES['message'].get_width()) / 2
        messsagey = int(SCREENHEIGHT * 0.13)
        basex = 0

        global last_background_change_time

        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                    return

            elapsed_time = pygame.time.get_ticks() - last_background_change_time

            if elapsed_time > CHANGE_BACKGROUND_INTERVAL:
                last_background_change_time = pygame.time.get_ticks()
                changeBackground()

            current_background = 'background_day' if elapsed_time % (2 * CHANGE_BACKGROUND_INTERVAL) < CHANGE_BACKGROUND_INTERVAL else 'background_night'
            SCREEN.blit(GAME_SPRITES[current_background], (0, 0))
            SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
            SCREEN.blit(GAME_SPRITES['message'], (messsagex, messsagex))
            SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
            pygame.display.update()
            FPSCLOCK.tick(FPS)

    def changeBackground():
        backgrounds = [BACKGROUND_DAY, BACKGROUND_NIGHT]
        new_background = pygame.image.load(random.choice(backgrounds)).convert()
        GAME_SPRITES['background'] = new_background

    def mainGame():
        score = 0
        playerx = int(SCREENWIDTH / 5)
        playery = int(SCREENWIDTH / 2)
        basex = 0
        newPipe1 = getRandomPipe()
        newPipe2 = getRandomPipe()

        upperPipes = [
            {'x': SCREENWIDTH + 200, 'y': newPipe1[0]['y']},
            {'x': SCREENWIDTH + 200 + (SCREENWIDTH / 2), 'y': newPipe2[0]['y']},
        ]
        lowerPipes = [
            {'x': SCREENWIDTH + 200, 'y': newPipe1[1]['y']},
            {'x': SCREENWIDTH + 200 + (SCREENWIDTH / 2), 'y': newPipe2[1]['y']},
        ]

        pipeVelX = -4

        playerVelY = -9
        playerMaxVelY = 10
        playerMinVelY = -8
        playerAccY = 1

        playerFlapAccv = -8
        playerFlapped = False
        flap_index = 0
        flap_delay = 5  # Delay for flapping animation

        while True:
            elapsed_time = pygame.time.get_ticks() - last_background_change_time
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                    if playery > 0:
                        playerVelY = playerFlapAccv
                        playerFlapped = True
                        GAME_SOUNDS['wing'].play()

            crashTest = isCollide(playerx, playery, upperPipes, lowerPipes)
            if crashTest:
                return

            playerMidPos = playerx + GAME_SPRITES['player'].get_width() / 2
            for pipe in upperPipes:
                pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width() / 2
                if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                    score += 1
                    print(f"Your score is {score}")
                    GAME_SOUNDS['point'].play()

            if playerVelY < playerMaxVelY and not playerFlapped:
                playerVelY += playerAccY

            if playerFlapped:
                if flap_delay == 0:
                    playerFlapped = False
                    flap_delay = 5
                else:
                    flap_delay -= 1

            playerHeight = GAME_SPRITES['player'].get_height()
            playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)

            for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
                upperPipe['x'] += pipeVelX
                lowerPipe['x'] += pipeVelX

            if 0 < upperPipes[0]['x'] < 5:
                newpipe = getRandomPipe()
                upperPipes.append(newpipe[0])
                lowerPipes.append(newpipe[1])

            if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
                upperPipes.pop(0)
                lowerPipes.pop(0)

            current_background = 'background_day' if elapsed_time % (2 * CHANGE_BACKGROUND_INTERVAL) < CHANGE_BACKGROUND_INTERVAL else 'background_night'
            SCREEN.blit(GAME_SPRITES[current_background], (0, 0))

            if playerFlapped:
                GAME_SPRITES['player'] = pygame.image.load(bird_flap_positions[flap_index]).convert_alpha()
                flap_index = (flap_index + 1) % len(bird_flap_positions)

            for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
                SCREEN.blit(GAME_SPRITES['pipe'][0], (upperPipe['x'], upperPipe['y']))
                SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerPipe['x'], lowerPipe['y']))

            SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
            SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))

            myDigits = [int(x) for x in list(str(score))]
            width = 0
            for digit in myDigits:
                width += GAME_SPRITES['numbers'][digit].get_width()
            Xoffset = (SCREENWIDTH - width) / 2

            for digit in myDigits:
                SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT * 0.12))
                Xoffset += GAME_SPRITES['numbers'][digit].get_width()

            pygame.display.update()
            FPSCLOCK.tick(FPS)

    def isCollide(playerx, playery, upperPipes, lowerPipes):
        if playery > GROUNDY - 25 or playery < 0:
            GAME_SOUNDS['hit'].play()
            return True

        for pipe in upperPipes:
            pipeHeight = GAME_SPRITES['pipe'][0].get_height()
            if playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
                GAME_SOUNDS['hit'].play()
                return True

        for pipe in lowerPipes:
            if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
                GAME_SOUNDS['hit'].play()
                return True

        return False

    def getRandomPipe():
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        offset = SCREENHEIGHT / 3
        y2 = offset + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height() - 1.2 * offset))
        pipeX = SCREENWIDTH + 10
        y1 = pipeHeight - y2 + offset
        pipe = [
            {'x': pipeX, 'y': -y1},  # upper Pipe
            {'x': pipeX, 'y': y2}  # lower Pipe
        ]
        return pipe

    if __name__ == '__main__':
        pygame.init()
        FPSCLOCK = pygame.time.Clock()
        pygame.display.set_caption('Flappy Bird By Swift Coders')
        GAME_SPRITES['numbers'] = (
            pygame.image.load('sprites/0.png').convert_alpha(),
            pygame.image.load('sprites/1.png').convert_alpha(),
            pygame.image.load('sprites/2.png').convert_alpha(),
            pygame.image.load('sprites/3.png').convert_alpha(),
            pygame.image.load('sprites/4.png').convert_alpha(),
            pygame.image.load('sprites/5.png').convert_alpha(),
            pygame.image.load('sprites/6.png').convert_alpha(),
            pygame.image.load('sprites/7.png').convert_alpha(),
            pygame.image.load('sprites/8.png').convert_alpha(),
            pygame.image.load('sprites/9.png').convert_alpha(),
        )
        GAME_SPRITES['message'] = pygame.image.load('sprites/message.png').convert_alpha()
        GAME_SPRITES['base'] = pygame.image.load('sprites/base.png').convert_alpha()
        GAME_SPRITES['pipe'] = (
            pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
            pygame.image.load(PIPE).convert_alpha()
        )
        GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()
        GAME_SPRITES['background_day'] = pygame.image.load(BACKGROUND_DAY).convert()
        GAME_SPRITES['background_night'] = pygame.image.load(BACKGROUND_NIGHT).convert()

        GAME_SOUNDS['die'] = pygame.mixer.Sound('audio/die.ogg')
        GAME_SOUNDS['hit'] = pygame.mixer.Sound('audio/hit.ogg')
        GAME_SOUNDS['point'] = pygame.mixer.Sound('audio/point.ogg')
        GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('audio/swoosh.ogg')
        GAME_SOUNDS['wing'] = pygame.mixer.Sound('audio/wing.ogg')

        while True:
            welcomeScreen()
            mainGame()
                   


def snake_game():
    import pygame,sys,random
    from pygame.math import Vector2

    class SNAKE:
        def __init__(self):
            self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
            self.direction = Vector2(0,0)
            self.new_block = False

            self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
            self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
            self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
            self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()
            
            self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
            self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
            self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
            self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

            self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
            self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

            self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
            self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
            self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
            self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()
            self.crunch_sound = pygame.mixer.Sound('Sound/crunch.wav')

        def draw_snake(self):
            self.update_head_graphics()
            self.update_tail_graphics()

            for index,block in enumerate(self.body):
                x_pos = int(block.x * cell_size)
                y_pos = int(block.y * cell_size)
                block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

                if index == 0:
                    screen.blit(self.head,block_rect)
                elif index == len(self.body) - 1:
                    screen.blit(self.tail,block_rect)
                else:
                    previous_block = self.body[index + 1] - block
                    next_block = self.body[index - 1] - block
                    if previous_block.x == next_block.x:
                        screen.blit(self.body_vertical,block_rect)
                    elif previous_block.y == next_block.y:
                        screen.blit(self.body_horizontal,block_rect)
                    else:
                        if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                            screen.blit(self.body_tl,block_rect)
                        elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                            screen.blit(self.body_bl,block_rect)
                        elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                            screen.blit(self.body_tr,block_rect)
                        elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                            screen.blit(self.body_br,block_rect)

        def update_head_graphics(self):
            head_relation = self.body[1] - self.body[0]
            if head_relation == Vector2(1,0): self.head = self.head_left
            elif head_relation == Vector2(-1,0): self.head = self.head_right
            elif head_relation == Vector2(0,1): self.head = self.head_up
            elif head_relation == Vector2(0,-1): self.head = self.head_down

        def update_tail_graphics(self):
            tail_relation = self.body[-2] - self.body[-1]
            if tail_relation == Vector2(1,0): self.tail = self.tail_left
            elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
            elif tail_relation == Vector2(0,1): self.tail = self.tail_up
            elif tail_relation == Vector2(0,-1): self.tail = self.tail_down

        def move_snake(self):
            if self.new_block == True:
                body_copy = self.body[:]
                body_copy.insert(0,body_copy[0] + self.direction)
                self.body = body_copy[:]
                self.new_block = False
            else:
                body_copy = self.body[:-1]
                body_copy.insert(0,body_copy[0] + self.direction)
                self.body = body_copy[:]

        def add_block(self):
            self.new_block = True

        def play_crunch_sound(self):
            self.crunch_sound.play()

        def reset(self):
            self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
            self.direction = Vector2(0,0)


    class FRUIT:
        def __init__(self):
            self.randomize()

        def draw_fruit(self):
            fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
            screen.blit(apple,fruit_rect)
            #pygame.draw.rect(screen,(126,166,114),fruit_rect)

        def randomize(self):
            self.x = random.randint(0,cell_number - 1)
            self.y = random.randint(0,cell_number - 1)
            self.pos = Vector2(self.x,self.y)

    class MAIN:
        def __init__(self):
            self.snake = SNAKE()
            self.fruit = FRUIT()

        def update(self):
            self.snake.move_snake()
            self.check_collision()
            self.check_fail()

        def draw_elements(self):
            self.draw_grass()
            self.fruit.draw_fruit()
            self.snake.draw_snake()
            self.draw_score()

        def check_collision(self):
            if self.fruit.pos == self.snake.body[0]:
                self.fruit.randomize()
                self.snake.add_block()
                self.snake.play_crunch_sound()

            for block in self.snake.body[1:]:
                if block == self.fruit.pos:
                    self.fruit.randomize()

        def check_fail(self):
            if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
                self.game_over()

            for block in self.snake.body[1:]:
                if block == self.snake.body[0]:
                    self.game_over()
            
        def game_over(self):
            self.snake.reset()

        def draw_grass(self):
            grass_color = (167,209,61)
            for row in range(cell_number):
                if row % 2 == 0: 
                    for col in range(cell_number):
                        if col % 2 == 0:
                            grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                            pygame.draw.rect(screen,grass_color,grass_rect)
                else:
                    for col in range(cell_number):
                        if col % 2 != 0:
                            grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                            pygame.draw.rect(screen,grass_color,grass_rect)			

        def draw_score(self):
            score_text = str(len(self.snake.body) - 3)
            score_surface = game_font.render(score_text,True,(56,74,12))
            score_x = int(cell_size * cell_number - 60)
            score_y = int(cell_size * cell_number - 40)
            score_rect = score_surface.get_rect(center = (score_x,score_y))
            apple_rect = apple.get_rect(midright = (score_rect.left,score_rect.centery))
            bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width + 6,apple_rect.height)

            pygame.draw.rect(screen,(167,209,61),bg_rect)
            screen.blit(score_surface,score_rect)
            screen.blit(apple,apple_rect)
            pygame.draw.rect(screen,(56,74,12),bg_rect,2)

    pygame.mixer.pre_init(44100,-16,2,512)
    pygame.init()
    cell_size = 40
    cell_number = 20
    screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
    clock = pygame.time.Clock()
    apple = pygame.image.load('Graphics/apple.png').convert_alpha()
    game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE,150)

    main_game = MAIN()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                main_game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if main_game.snake.direction.y != 1:
                        main_game.snake.direction = Vector2(0,-1)
                if event.key == pygame.K_RIGHT:
                    if main_game.snake.direction.x != -1:
                        main_game.snake.direction = Vector2(1,0)
                if event.key == pygame.K_DOWN:
                    if main_game.snake.direction.y != -1:
                        main_game.snake.direction = Vector2(0,1)
                if event.key == pygame.K_LEFT:
                    if main_game.snake.direction.x != 1:
                        main_game.snake.direction = Vector2(-1,0)

        screen.fill((175,215,70))
        main_game.draw_elements()
        pygame.display.update()
        clock.tick(60)


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == K_1:
                current_game = FLAPPY_BIRD
                change_game = True
            elif event.key == K_2:
                current_game = SNAKE_GAME
                change_game = True

    if change_game:
        # Reset variables or perform any necessary setup for the selected game
        if current_game == FLAPPY_BIRD:
            # Reset Flappy Bird variables
            pass     
        elif current_game == SNAKE_GAME:
            # Reset Snake game variables
            pass

        change_game = False

    SCREEN.fill((255, 255, 255))  # Change to the background color you prefer

    if current_game == WELCOME_SCREEN:
        welcome_screen()
    elif current_game == FLAPPY_BIRD:
        flappy_bird_game()
    elif current_game == SNAKE_GAME:
        snake_game()

    pygame.display.update()
    FPSCLOCK.tick(FPS)
