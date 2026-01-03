import pygame
import random
import sys

# initialize pygame
pygame.init()

# screen size
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# clock & speed
clock = pygame.time.Clock()
SNAKE_BLOCK = 10
SNAKE_SPEED = 15

# font
font = pygame.font.SysFont("arial", 25)


def show_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))


def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], SNAKE_BLOCK, SNAKE_BLOCK])


def game_loop():
    game_over = False
    game_close = False

    x1 = WIDTH // 2
    y1 = HEIGHT // 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    foodx = random.randrange(0, WIDTH - SNAKE_BLOCK, 10)
    foody = random.randrange(0, HEIGHT - SNAKE_BLOCK, 10)

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            msg = font.render("Game Over! Press C-Play Again or Q-Quit", True, RED)
            screen.blit(msg, (50, HEIGHT // 2))
            show_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_list)
        show_score(snake_length - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = random.randrange(0, WIDTH - SNAKE_BLOCK, 10)
            foody = random.randrange(0, HEIGHT - SNAKE_BLOCK, 10)
            snake_length += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    sys.exit()


game_loop()
