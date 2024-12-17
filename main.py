import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Maze Game")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont("Arial", 25)

def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def create_food(snake, maze):
    while True:
        x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        if (x, y) not in snake and (x, y) not in maze:
            return (x, y)

def create_maze():
    maze = []
    for _ in range(20):
        x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        maze.append((x, y))
    return maze

def game_over():
    screen.fill(BLACK)
    draw_text("Game Over! Press R to Restart or Q to Quit", RED, WIDTH // 8, HEIGHT // 2)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

def main():
    # Snake initialization
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = "RIGHT"
    change_to = direction

    # Food and maze
    food = create_food(snake, [])
    maze = create_maze()

    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    change_to = "UP"
                if event.key == pygame.K_DOWN and direction != "UP":
                    change_to = "DOWN"
                if event.key == pygame.K_LEFT and direction != "RIGHT":
                    change_to = "LEFT"
                if event.key == pygame.K_RIGHT and direction != "LEFT":
                    change_to = "RIGHT"

        # Change direction
        direction = change_to

        # Move snake
        x, y = snake[0]
        if direction == "UP":
            y -= CELL_SIZE
        if direction == "DOWN":
            y += CELL_SIZE
        if direction == "LEFT":
            x -= CELL_SIZE
        if direction == "RIGHT":
            x += CELL_SIZE

        new_head = (x, y)

        # Check for collisions
        if (
            x < 0
            or x >= WIDTH
            or y < 0
            or y >= HEIGHT
            or new_head in snake
            or new_head in maze
        ):
            game_over()

        # Add new head to snake
        snake.insert(0, new_head)

        # Check if snake eats food
        if new_head == food:
            score += 1
            food = create_food(snake, maze)
        else:
            snake.pop()  # Remove tail if no food eaten

        # Draw everything
        screen.fill(BLACK)
        for segment in snake:
            pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))

        pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], CELL_SIZE, CELL_SIZE))

        for wall in maze:
            pygame.draw.rect(screen, BLUE, pygame.Rect(wall[0], wall[1], CELL_SIZE, CELL_SIZE))

        draw_text(f"Score: {score}", WHITE, 10, 10)
        pygame.display.flip()

        # Control game speed
        clock.tick(5)

if __name__ == "__main__":
    main()




