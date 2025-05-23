import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
SPEED = 6

# Set up some color
BROWN= (139, 69, 19)
TURQUOISE = (0, 199, 140)
YELLOW = (255, 255, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the snake
snake = [(200, 200), (220, 200), (240, 200)]

# Set up the food
food = (400, 300)

# Set up the direction
direction = 'RIGHT'

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

    # Move the snake
    head = snake[-1]
    if direction == 'UP':
        new_head = (head[0], head[1] - GRID_SIZE)
    elif direction == 'DOWN':
        new_head = (head[0], head[1] + GRID_SIZE)
    elif direction == 'LEFT':
        new_head = (head[0] - GRID_SIZE, head[1])
    elif direction == 'RIGHT':
        new_head = (head[0] + GRID_SIZE, head[1])
    snake.append(new_head)

    # Check for collision with wall or self
    if (snake[-1][0] < 0 or snake[-1][0] >= WIDTH or
            snake[-1][1] < 0 or snake[-1][1] >= HEIGHT or
            snake[-1] in snake[:-1]):
        print("Game over!")
        pygame.quit()
        sys.exit()

    # Check for food
    if snake[-1] == food:
        food = (random.randint(0, WIDTH - GRID_SIZE) // GRID_SIZE * GRID_SIZE,
                random.randint(0, HEIGHT - GRID_SIZE) // GRID_SIZE * GRID_SIZE)
    else:
        snake.pop(0)

    # Draw everything
    screen.fill(BROWN)
    for x, y in snake:
        pygame.draw.rect(screen, TURQUOISE, (x, y, GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(screen, YELLOW, (food[0], food[1], GRID_SIZE, GRID_SIZE))
    text = font.render(f"Score: {len(snake)}", True, TURQUOISE)
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.delay(1000 // SPEED)
