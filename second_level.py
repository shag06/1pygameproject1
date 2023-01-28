import os
import time

import pygame
import sys
from pausing import pause
from Classes import Willy, Bullet, Boss, load_image, Cur


class SecondLevel:
    def __init__(self):
        self.size = width, height = 1000, 800
        self.screen = pygame.display.set_mode(self.size)
        self.bg = load_image('data/images/ScaledBG.png')
        self.clock = pygame.time.Clock()

        size_of_hero = (82, 100)
        self.coords_for_ghosts = [[0, 0], [0, self.size[1] - size_of_hero[1]], [self.size[0] - size_of_hero[0], 0],
                                  [self.size[0] - size_of_hero[0], self.size[1] - size_of_hero[1]]]

        # Группы пуль разных персонажей (Чтобы не попадали своей пулей в себя)
        self.boss_bullets = []
        self.willy_bullets = []
        self.willy = Willy(400, 400, self.clock)
        self.boss = Boss()

    def progressbar_willy(self):
        color = pygame.Color('green')
        color2 = pygame.Color("black")
        scale_lengths = (200 * self.willy.HP) / 1400
        pygame.draw.rect(self.screen, color2, (750, 20, 200, 10))
        pygame.draw.rect(self.screen, color, (750, 22, scale_lengths, 6))

    def progressbar_boss(self):
        color = pygame.Color('red')
        color2 = pygame.Color("black")
        scale_lengths = (200 * self.boss.HP) / 1000
        pygame.draw.rect(self.screen, color2, (50, 20, 200, 10))
        pygame.draw.rect(self.screen, color, (50, 22, scale_lengths, 6))

    def play(self):
        pygame.init()
        pygame.display.set_caption("No peace for Willy")

        running = True
        clock = time.time()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pause(self.willy, [self.boss])
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
                    # Выстрел игрока
                    self.willy_bullets.append(Bullet((self.willy.x, self.willy.y),
                                                     event.pos, self.willy_bullets, self.clock))
            # Автоматический выстрел босса
            if int(clock) + 1 == int(time.time()):
                self.boss_bullets.append(Bullet((self.boss.x + 130, self.boss.y + 190),
                                                (self.willy.x, self.willy.y), self.boss_bullets, self.clock))
                clock = time.time()
            # Проверка попадания в босса и в игрока
            for i in self.willy_bullets:
                i.hit(self.boss)
            for i in self.boss_bullets:
                i.hit(self.willy)

            # Обновление параметров
            self.willy.moving()
            self.willy.update()
            self.boss.update()

            self.progressbar_willy()
            self.progressbar_boss()

            for i in self.boss_bullets:
                i.update()
            for i in self.willy_bullets:
                i.update()

            # Обновление отображения
            self.screen.blit(self.bg, (0, 0))
            self.screen.blit(self.willy.image, self.willy.rect)
            self.screen.blit(self.boss.image, self.boss.rect)
            for bullet in self.boss_bullets:
                self.screen.blit(bullet.image, bullet.rect)
            for bullet in self.willy_bullets:
                self.screen.blit(bullet.image, bullet.rect)
            pygame.display.flip()
        quit()


if __name__ == "__main__":
    game = SecondLevel()
    game.play()
