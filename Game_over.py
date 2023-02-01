import pygame
from PIL import Image
import time


def game_lose():
    pygame.init()
    size = width, height = 1000, 800
    screen = pygame.display.set_mode(size)
    pygame.display.flip()
    running = True
    clock = time.time()
    clock2 = time.time()
    color1 = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        im = Image.open("data/images/game_over_paint.jpg")
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                k = 230
                if r > k and g > k and b > k:
                    r = g = b = color1
                pixels[i, j] = r, g, b
        if int(clock) + 1 == int(time.time()):
            if color1 < 250:
                 color1 += 50
            else:
                background_image = pygame.image.load('data/images/heart2.jpg')
                screen.blit(background_image, [0, 500])
            clock = time.time()
        im.save("data/images/Game_over_paint_2.png")
        background_image = pygame.image.load('data/images/Game_over_paint_2.png')
        screen.blit(background_image, [0, 0])
        pygame.display.update()
        if int(time.time()) - int(clock2) >= 10:
            running = False


if __name__ == "__main__":
    game_lose()
