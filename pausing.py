import datetime
import sqlite3
import pygame
import sys

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

    def checkForInput(self, position, number, *data):
        global running
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            if number == 1:
                print("Unpausing...")
                running = False
            if number == 2:
                willy = data[0]
                ghosts = data[1]
                count = data[2]
                date = datetime.datetime.now()
                hp_willy = str(willy.HP)
                hp_ghosts = " ".join([str(gh.HP) for gh in ghosts])
                pos_willy = " ".join([str(willy.x), str(willy.y)])
                pos_ghosts = " ".join(sum([[str(elem) for elem in gh.pos] for gh in ghosts], []))
                db = "data\\databases\\saving.sqlite"
                con = sqlite3.connect(db)
                cur = con.cursor()
                willy_id = 1
                l = cur.execute(f"""SELECT id from save WHERE id = {willy_id}""").fetchone()
                while l:
                    willy_id += 1
                    l = cur.execute(f"""SELECT id from save WHERE id = {willy_id}""").fetchone()
                cur.execute(f"""
                INSERT INTO save(id, date, pos_willy, pos_ghosts, hp_willy, hp_ghosts, count) 
                VALUES ({willy_id}, "{date}", "{pos_willy}", "{pos_ghosts}", "{hp_willy}", "{hp_ghosts}", {count})
                """)
                con.commit()
                print("Game saved")
            if number == 3:
                print("Main menu!")
                return False
        return True


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
running = True
buttons = [button1, button2, button3]


def pause(willy, ghosts, count):
    global running
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
                break
            if event.type == pygame.QUIT:

                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                button1.checkForInput(pygame.mouse.get_pos(), 1)
                # game = FirstLevel()
                # game.play()
                button2.checkForInput(pygame.mouse.get_pos(), 2, willy, ghosts, count)
                res = button3.checkForInput(pygame.mouse.get_pos(), 3)
                if not res:
                    print("return False")
                    return False
        background_image = pygame.image.load('data/images/ScaledBG.png')
        screen.blit(background_image, [0, 0])
        for b in buttons:
            b.update()
            b.changeColor(pygame.mouse.get_pos())
        pygame.display.update()


if __name__ == "__main__":
    print("errror")
    willy = []
    ghosts = []
    W = Willy(1, 1, 1)
    G = Ghost(1, 0, 1, 1, 1)
    pause(W, [G for i in range(4)])