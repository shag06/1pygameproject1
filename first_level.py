import pygame
import random

from Classes import Willy, Bullet, Ghost, load_image
from pausing import pause


class FirstLevel:
    def __init__(self):
        self.size = width, height = 1000, 800
        self.screen = pygame.display.set_mode(self.size)
        self.bg = load_image('data/images/ScaledBG.png')
        self.clock = pygame.time.Clock()

        self.bullets = []
        self.willy = Willy(400, 400, self.clock)

        # Группа спрайтов призраки
        size_of_hero = (82, 100)
        self.ghosts = []
        self.coords_for_ghosts = [[0, 0], [0, self.size[1] - size_of_hero[1]], [self.size[0] - size_of_hero[0], 0],
                             [self.size[0] - size_of_hero[0], self.size[1] - size_of_hero[1]]]
        for i in range(4):
            self.ghosts.append(Ghost(*self.coords_for_ghosts[i], self.ghosts, self.willy, self.clock))

    def progressbar_willy(self):
        color = pygame.Color('green')
        color2 = pygame.Color("black")
        scale_lengths = (200 * self.willy.HP) / 1400
        pygame.draw.rect(self.screen, color2, (750, 20, 200, 10))
        pygame.draw.rect(self.screen, color, (750, 22, scale_lengths, 6))

    def progressbar_ghost(self):
        color = pygame.Color('red')
        color2 = pygame.Color("black")
        k = 1
        y = 20
        for i in self.ghosts:
            scale_lengths = (200 * i.HP) / 350
            pygame.draw.rect(self.screen, color2, (50, y, 200, 10))
            pygame.draw.rect(self.screen, color, (50, y + 2, scale_lengths, 6))
            y = y + 12
            k += 1

    def play(self):
        pygame.init()
        pygame.display.set_caption("No peace for Willy")

        running = True
        pausing = False
        while running:
            if not pausing:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        pause(self.willy, self.ghosts)
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            self.willy.move_left = True
                        elif event.key == pygame.K_d:
                            self.willy.move_right = True
                        elif event.key == pygame.K_w:
                            self.willy.move_forward = True
                        elif event.key == pygame.K_s:
                            self.willy.move_backwards = True

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_a:
                            self.willy.move_left = False
                        elif event.key == pygame.K_d:
                            self.willy.move_right = False
                        elif event.key == pygame.K_w:
                            self.willy.move_forward = False
                        elif event.key == pygame.K_s:
                            self.willy.move_backwards = False

                    if event.type == pygame.MOUSEBUTTONUP:
                        self.bullets.append(Bullet((self.willy.x, self.willy.y), event.pos, self.bullets, self.clock))

                self.willy.moving()
                self.willy.update()

                for j in self.ghosts:
                    for i in self.bullets:
                        i.hit(j)
                    is_living = j.update((self.willy.x, self.willy.y))
                    if not is_living:
                        self.ghosts.append(Ghost(*self.coords_for_ghosts[random.randint(0, 3)],
                                                 self.ghosts, self.willy, self.clock))
                for i in self.bullets:
                    i.update()

                self.screen.blit(self.bg, (0, 0))
                self.screen.blit(self.willy.image, self.willy.rect)
                for ghost in self.ghosts:
                    self.screen.blit(ghost.image, ghost.rect)
                for bullet in self.bullets:
                    self.screen.blit(bullet.image, bullet.rect)

                # количество жизней у willy
                self.progressbar_willy()
                # количество жизней у ghost
                self.progressbar_ghost()
            else:
                for event in pygame.event.get():
                    if event.type == pygame.K_ESCAPE:
                        pausing = False

            pygame.display.flip()
        quit()


if __name__ == "__main__":
    game = FirstLevel()
    game.play()
