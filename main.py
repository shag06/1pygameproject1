import pygame
import sys
import first_level as fl

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Button!")
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
                print("New game!")
                fl.start_level()
            if number == 2:
                print("Get game!")
            if number == 3:
                print("About game!")

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and \
                position[1] in range(self.rect.top, self.rect.bottom):
            self.text = main_font.render(self.text_input, True, "green")
        else:
            self.text = main_font.render(self.text_input, True, "white")


button_surface = pygame.image.load("button.png")
size1 = (300, 100)
size2 = (375, 100)
size3 = (275, 100)
button_surface1 = pygame.transform.scale(button_surface, size1)
button_surface2 = pygame.transform.scale(button_surface, size2)
button_surface3 = pygame.transform.scale(button_surface, size3)
button1 = Button(button_surface1, 400, 175, "Новая игра")
button2 = Button(button_surface2, 400, 370, "Загрузить игру")
button3 = Button(button_surface3, 400, 550, "Об игре")

if __name__ == "__main__":
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                button1.checkForInput(pygame.mouse.get_pos(), 1)
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