import pygame
import sys
from first_level import FirstLevel

pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("No peace for Willy!")
main_font = pygame.font.SysFont("cambria", 45)


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

    def checkForInput(self, position, number):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            if number == 1:
                print("Unpausing...")
            if number == 2:
                print("Game saved")
            if number == 3:
                print("Main menu!")

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and \
                position[1] in range(self.rect.top, self.rect.bottom):
            self.text = main_font.render(self.text_input, True, "green")
        else:
            self.text = main_font.render(self.text_input, True, "white")


button_surface = pygame.image.load("data\\images\\button.png")
size1 = (450, 100)
size2 = (450, 100)
size3 = (450, 100)
button_surface1 = pygame.transform.scale(button_surface, size1)
button_surface2 = pygame.transform.scale(button_surface, size2)
button_surface3 = pygame.transform.scale(button_surface, size3)
button1 = Button(button_surface1, 500, 175, "Возобновить игру")
button2 = Button(button_surface2, 500, 370, "Сохранить игру")
button3 = Button(button_surface3, 500, 550, "В главное меню")

def pause():
    if __name__ == "__main__":
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    button1.checkForInput(pygame.mouse.get_pos(), 1)
                    game = FirstLevel()
                    game.play()
                    button2.checkForInput(pygame.mouse.get_pos(), 2)
                    button3.checkForInput(pygame.mouse.get_pos(), 3)
            screen.fill("black")
            button1.update()
            button1.changeColor(pygame.mouse.get_pos())
            button2.update()
            button2.changeColor(pygame.mouse.get_pos())
            button3.update()
            button3.changeColor(pygame.mouse.get_pos())
            pygame.display.update()

pause()