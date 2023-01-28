import pygame_widgets
from pygame_widgets.progressbar import ProgressBar
import pygame

pygame.init()
win = pygame.display.set_mode((1000, 600))

progressBar = ProgressBar(win, 30, 10, 100, 7, lambda: 0.5, curved=True,
                          completedColour=(255, 0, 0), incompletedColour=(0, 0, 0))
progressBar2 = ProgressBar(win, 30, 20, 100, 7, lambda: 0.5, curved=True,
                           completedColour=(255, 0, 0), incompletedColour=(0, 0, 0))
progressBar3 = ProgressBar(win, 30, 30, 100, 7, lambda: 0.5, curved=True,
                           completedColour=(255, 0, 0), incompletedColour=(0, 0, 0))
progressBar4 = ProgressBar(win, 30, 40, 100, 7, lambda: 0.5, curved=True,
                           completedColour=(255, 0, 0), incompletedColour=(0, 0, 0))
progressBar5 = ProgressBar(win, 30, 50, 100, 7, lambda: 0.5, curved=True,
                           completedColour=(255, 0, 0), incompletedColour=(0, 0, 0))
progressBar6 = ProgressBar(win, 870, 10, 100, 7, lambda: 0.5, curved=True,
                           completedColour=(0, 0, 255), incompletedColour=(0, 0, 0))

run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()

    win.fill((255, 255, 255))

    pygame_widgets.update(events)
    pygame.display.flip()