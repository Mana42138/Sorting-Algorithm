import pygame
import random
import sys

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
BAR_WIDTH = 15
BAR_SPACING = 2
WHITE = (25,25,25)
COLOR_DRAW = (100, 255, 100)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bubble Sort Visualization")

def draw_data(data, swapped_indexes):
    screen.fill(WHITE)
    for i in range(len(data)):
        color = COLOR_DRAW if i in swapped_indexes else WHITE
        pygame.draw.rect(screen, color, (i * (BAR_WIDTH + BAR_SPACING), SCREEN_HEIGHT - data[i], BAR_WIDTH, data[i]))
    pygame.display.update()

def bubble_sort(data):
    n = len(data)
    swapped = True
    while swapped:
        swapped = False
        swapped_indexes = []
        for i in range(1, n):
            if data[i - 1] > data[i]:
                data[i - 1], data[i] = data[i], data[i - 1]
                swapped = True
                swapped_indexes.extend([i - 1, i])
                draw_data(data, swapped_indexes)
                pygame.time.delay(10)

def main():
    data = [random.randint(50, SCREEN_HEIGHT - 20) for _ in range(SCREEN_WIDTH // (BAR_WIDTH + BAR_SPACING))]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        bubble_sort(data)
        running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
