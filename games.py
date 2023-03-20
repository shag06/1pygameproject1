import datetime
import sqlite3
import pygame
import sys
from Classes import Willy, Ghost, start_level_from_data

pygame.init()
re = []
running = True
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("No peace for Willy!")
main_font = pygame.font.SysFont("cambria", 30)


class Button:
    def __init__(self, image, x_pos, y_pos, text_input):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = main_font.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position, number, *data):
        global running
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            if number == -1:
                print("Unpausing...")
                running = False
            else:
                data = re[number]
                print(data)
                running = False
                start_level_from_data(data)


    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and \
                position[1] in range(self.rect.top, self.rect.bottom):
            self.text = main_font.render(self.text_input, True, "green")
        else:
            self.text = main_font.render(self.text_input, True, "white")


def get_games():
    global running, re
    db = "data\\databases\\saving.sqlite"
    con = sqlite3.connect(db)
    cur = con.cursor()
    re = cur.execute(f"""SELECT * from save""").fetchall()
    res = [" ".join([str(k) for k in [e[1]]])[:-7] for e in re] + ["Выйти в окно"]
    res.reverse()
    koord = 100
    buttons = []
    button_surface = pygame.image.load("data\\images\\button.png")
    size = (400, 75)
    button_surface = pygame.transform.scale(button_surface, size)
    k = 250
    for e in res:
        button = Button(button_surface, k, koord, e)
        buttons.append(button)
        koord += 125
        if koord > 1000:
            k += 500
            koord = 100
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
                break
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(buttons)):
                    ind = -1 if i == 0 else len(buttons) - i - 1
                    buttons[i].checkForInput(pygame.mouse.get_pos(), ind)
        background_image = pygame.image.load('data/images/ScaledBG.png')
        screen.blit(background_image, [0, 0])
        ind = 0
        for button in buttons:
            button.update()
            button.changeColor(pygame.mouse.get_pos())
            ind += 1
        pygame.display.update()
    print(res)


if __name__ == "__main__":
    get_games()