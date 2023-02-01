import pygame
from PIL import Image
import time


def you_win(img):
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
        im = Image.open(img)
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                if pixels[i, j] == (255, 255, 255):
                    pixels[i, j] = (color1, color1, color1)
        if int(clock) + 1 == int(time.time()):
            if color1 < 250:
                 color1 += 50
            else:
                background_image = pygame.image.load(img)
                screen.blit(background_image, [0, 500])
            clock = time.time()
        im.save(img)
        background_image = pygame.image.load(img)
        screen.blit(background_image, [0, 0])
        pygame.display.update()
        if int(time.time()) - int(clock2) >= 5:
            running = False


if __name__ == "__main__":
    you_win("data/images/game_win.jpg")
