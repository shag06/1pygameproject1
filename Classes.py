import os
import os
import time
from game_won import you_win
import pygame
import sys
from pausing import pause
import sys
from Game_over import game_lose
from game_won import you_win
import pygame
import random
from pausing import pause
from game_won import you_win
from Game_over import game_lose


# Класс главного персонажа
class Willy(pygame.sprite.Sprite):
    # Инициализация
    def __init__(self, x, y, wall, clock, hp):
        self.wall = wall
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        # Скорость движения
        self.speed = 1
        # Параметр для анимации движения
        self.LENGTH = 4
        self.HP = hp

        # Импорт картинок для анимации движения
        self.images_face = [f'data/images/hero/face{i}.png' for i in range(4)]
        self.images_back = [f'data/images/hero/back{i}.png' for i in range(4)]
        self.images_left = [f'data/images/hero/left{i}.png' for i in range(4)]
        self.images_right = [f'data/images/hero/right{i}.png' for i in range(4)]

        self.image = pygame.transform.scale(load_image(self.images_face[0]), (82, 100))

        # Моделька

        self.rect = self.image.get_rect(topleft=(x, y))

        # Создания флагов проверки направления движения и соответственных счётчиков
        self.move_forward = False
        self.counter_w = 0

        self.move_backwards = False
        self.counter_s = 0

        self.move_left = False
        self.counter_a = 0

        self.move_right = False
        self.counter_d = 0

    # Обновление модельки
    def update(self, *args):
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        if self.HP <= 0:
            game_lose()
            sys.exit()

    # Функция движения
    def moving(self):
        # -------------------------------
        for i in self.wall:
            if self.rect.colliderect(i):
                if self.move_left:
                    self.x += 10
                elif self.move_right:
                    self.x -= 10
                if self.move_forward:
                    self.y += 10
                elif self.move_backwards:
                    self.y -= 10
        # ------------------------------
        # Проверка направления по флагам и соответствующие изменения координат
        if self.move_forward:
            self.image = pygame.transform.scale(load_image(self.images_back[self.counter_w]), (82, 100))
            self.counter_w = (self.counter_w + 1) % self.LENGTH
            if self.y <= self.speed:
                self.y = 0
            else:
                self.y -= self.speed
        if self.move_backwards:
            self.image = pygame.transform.scale(load_image(self.images_face[self.counter_s]), (82, 100))
            self.counter_s = (self.counter_s + 1) % self.LENGTH
            if self.y + 100 >= 800 - self.speed:
                self.y = 700
            else:
                self.y += self.speed
        if self.move_left:
            self.image = pygame.transform.scale(load_image(self.images_left[self.counter_a]), (82, 100))
            self.counter_a = (self.counter_a + 1) % self.LENGTH
            if self.x <= self.speed:
                self.x = 0
            else:
                self.x -= self.speed
        if self.move_right:
            self.image = pygame.transform.scale(load_image(self.images_right[self.counter_d]), (82, 100))
            self.counter_d = (self.counter_d + 1) % self.LENGTH
            if self.x + 82 >= 1000 - self.speed:
                self.x = 918
            else:
                self.x += self.speed


# Класс снаряда
class Bullet(pygame.sprite.Sprite):
    # Инициализация
    def __init__(self, pos, target, group, clock):
        self.group = group
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(load_image('data/images/newBullet.png',
                                                       colorkey=pygame.Color("WHITE")), (70, 70))
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        # Точка нажатия при выстреле, по ней формируется направление полёта пули
        self.target = target
        self.SPEED = 2
        self.DAMAGE = 25

        self.rect = self.image.get_rect(topleft=pos)

    def update(self, *args):
        # Мат.модель полёта пули
        if self.pos[1] == self.target[1]:
            if self.pos[0] >= self.target[0]:
                self.x -= self.SPEED
            else:
                self.x += self.SPEED
        elif self.pos[0] == self.target[0]:
            if self.pos[1] > self.target[1]:
                self.y -= self.SPEED
            else:
                self.y += self.SPEED
        else:
            tg = abs((self.target[0] - self.pos[0]) / (self.target[1] - self.pos[1]))
            b = ((self.SPEED / (1 + tg ** 2)) ** 0.5)
            a = ((self.SPEED / (1 + tg ** 2)) ** 0.5) * tg
            if self.target[0] > self.pos[0] and self.target[1] > self.pos[1]:
                self.x += a
                self.y += b
            elif self.target[1] - self.pos[1] > 0 > self.target[0] - self.pos[0]:
                self.x -= a
                self.y += b
            elif self.target[0] < self.pos[0] and self.target[1] < self.pos[1]:
                self.x -= a
                self.y -= b
            else:
                self.x += a
                self.y -= b

        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    # Функция попадания по врагу
    def hit(self, enemy):
        if self.rect.colliderect(enemy.rect):
            enemy.HP -= self.DAMAGE
            self.kill()
            self.group.remove(self)
        else:
            pass


# Класс призрака
class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y, group, willy, clock, hp):
        pygame.sprite.Sprite.__init__(self)
        self.pos = (x, y)
        self.speed = 0.08
        self.HP = hp
        self.group = group
        self.LENGTH = 3
        self.DAMAGE = 1
        self.willy = willy

        self.images_face = [f'data/images/ghost/face{i}.png' for i in range(self.LENGTH)]
        self.images_back = [f'data/images/ghost/back{i}.png' for i in range(self.LENGTH)]
        self.images_left = [f'data/images/ghost/left{i}.png' for i in range(self.LENGTH)]
        self.images_right = [f'data/images/ghost/right{i}.png' for i in range(self.LENGTH)]

        self.image = pygame.transform.scale(load_image(self.images_face[0]), (82, 100))

        self.rect = self.image.get_rect(topleft=(x, y))
        self.move_forward = False
        self.counter_w = 0

        self.move_backwards = False
        self.counter_s = 0

        self.move_left = False
        self.counter_a = 0

        self.move_right = False
        self.counter_d = 0

    # Функция обновления движения призрака и проверка смерти призрака
    def update(self, *args):
        if self.rect.colliderect(self.willy):
            self.rect = self.image.get_rect(topleft=(self.pos))
            self.willy.HP -= self.DAMAGE
            return True
        else:
            # Если призрак жив, то его позиция меняется (Аналогично пули, только target - наш персонаж)
            if self.HP > 0:
                self.target = args[0]
                x, y = self.pos[0], self.pos[1]
                if self.pos[1] == self.target[1]:
                    if self.pos[0] >= self.target[0]:
                        x -= self.speed
                    else:
                        x += self.speed
                else:
                    tg = abs((self.target[0] - self.pos[0]) / (self.target[1] - self.pos[1]))
                    b = ((self.speed / (1 + tg ** 2)) ** 0.5)
                    a = ((self.speed / (1 + tg ** 2)) ** 0.5) * tg

                    if self.target[0] > self.pos[0] + 10 and self.target[1] > self.pos[1] + 10:
                        self.image = pygame.transform.scale(load_image(self.images_face[self.counter_w // 3]),
                                                            (82, 100))
                        self.counter_w += 1
                        self.counter_w %= (self.LENGTH * 3)
                        x += a
                        y += b
                    elif self.target[1] - self.pos[1] > 10 > self.target[0] - self.pos[0]:
                        self.image = pygame.transform.scale(load_image(self.images_left[self.counter_a // 3]),
                                                            (82, 100))
                        self.counter_a += 1
                        self.counter_a %= (self.LENGTH * 3)
                        x -= a
                        y += b
                    elif self.target[0] < self.pos[0] + 10 and self.target[1] < self.pos[1] + 10:
                        self.image = pygame.transform.scale(load_image(self.images_right[self.counter_s // 3]),
                                                            (82, 100))
                        self.counter_s += 1
                        self.counter_s %= (self.LENGTH * 3)
                        x -= a
                        y -= b
                    else:
                        self.image = pygame.transform.scale(load_image(self.images_left[self.counter_d // 3]),
                                                            (82, 100))
                        self.counter_d += 1
                        self.counter_d %= (self.LENGTH * 3)
                        x += a
                        y -= b
                self.pos = (x, y)
                self.rect = self.image.get_rect(topleft=(x, y))
                return True
            else:
                self.kill()
                self.group.remove(self)
                return False


# Класс боса
class Boss(pygame.sprite.Sprite):
    def __init__(self, hp):
        pygame.sprite.Sprite.__init__(self)
        self.x = 300
        self.y = 0
        self.pos = (self.x, self.y)
        self.HP = hp

        image = load_image('data/images/VVP1.png')
        self.image = pygame.transform.scale(image, (300, 200))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update(self):
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        if self.HP <= 0:
            you_win("data/images/game_win.jpg")
            sys.exit()


# Курсор
class Cur(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        image = load_image('data/images/arrow.png')
        self.image = pygame.transform.scale(image, (60, 50))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update(self, *args):
        self.x = args[0][0]
        self.y = args[0][1]
        self.rect = self.image.get_rect(topleft=(self.x, self.y))


# Выгрузка изображений
def load_image(name, colorkey=pygame.Color("WHITE")):
    fullname = os.path.join('', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname).convert()
    image.set_colorkey(colorkey)
    return image


class Boss_bullet(Bullet):
    def __init__(self, pos, target, group, clock):
        super().__init__(pos, target, group, clock)
        self.image = pygame.transform.scale(load_image('data/images/BossBullet.png',
                                                       colorkey=pygame.Color("WHITE")), (70, 70))
        self.DAMAGE = 200


# -------------------------------------------------
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.pos = (x, y)
        self.HP = 100000
        pygame.sprite.Sprite.__init__(self)
        image = load_image('data/images/wall3.png')
        self.image = pygame.transform.scale(image, (180, 40))
        self.rect = self.image.get_rect(topleft=self.pos)
# ----------------------------------------------------


def start_level_from_data(data):
    # first (5, '2023-01-29 00:18:04.165966', '400.0 375.0', '55.08 53.2 60.4 652.9 856.6 45.9 852.3 660.42', '1400', '350 350 350 350')
    # second (13, '2023-02-01 15:23:48.527053', '841.5 453.5', '300 0', '1275', '975')
    hp_willy = int(data[-3])
    pos_willy = list(map(float, data[2].split()))
    hp_ghosts = list(map(int, data[5].split()))
    count = int(data[6])
    if len(hp_ghosts) == 4:
        pos_ghosts = list(map(float, data[3].split()))
        game = FirstLevel(pos_willy, pos_ghosts, hp_willy, hp_ghosts, count)
    else:
        hp_boss = hp_ghosts[-1]
        game = SecondLevel(pos_willy, hp_willy, hp_boss)
    game.play()


class FirstLevel:
    def __init__(self, pos_willy=(400, 400), pos_ghosts=None, hp_willy=1400, hp_ghosts=(350, 350, 350, 350), count=0):
        const_gh = 10
        self.counter = const_gh
        self.count = count
        self.size = width, height = 1000, 800
        size_of_hero = (82, 100)
        if pos_ghosts is None:
            pos_ghosts = [[0, 0], [0, self.size[1] - size_of_hero[1]], [self.size[0] - size_of_hero[0], 0],
                          [self.size[0] - size_of_hero[0], self.size[1] - size_of_hero[1]]]
        self.size = width, height = 1000, 800
        self.screen = pygame.display.set_mode(self.size)
        self.bg = load_image('data/images/ScaledBG.png')
        self.clock = pygame.time.Clock()
        # ------------------------------------------
        self.wall = []
        wall_coords = []
        o = 1
        o1 = True
        while o != 8:
            x = random.randrange(100, 900)
            y = random.randrange(100, 900)
            for i in wall_coords:
                if i[0] == x and i[1] == y:
                    o1 = False
            if o1:
                self.wall.append(Wall(x, y))
                wall_coords.append((x, y))
                o += 1
        # ------------------------------------------

        self.bullets = []
        self.willy = Willy(*pos_willy, self.wall, self.clock, hp_willy)

        # Группа спрайтов призраки

        self.ghosts = []
        self.coords_for_ghosts = [[0, 0], [0, self.size[1] - size_of_hero[1]], [self.size[0] - size_of_hero[0], 0],
                             [self.size[0] - size_of_hero[0], self.size[1] - size_of_hero[1]]]
        for i in range(4):
            self.ghosts.append(Ghost(*self.coords_for_ghosts[i], self.ghosts, self.willy, self.clock, hp_ghosts[i]))

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
        count = 1
        while running and count <= self.counter and self.willy.HP > 0:
            if not pausing:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        res = pause(self.willy, self.ghosts, self.count)
                        if not res:
                            running = False
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

                    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        self.bullets.append(Bullet((self.willy.x, self.willy.y), event.pos, self.bullets, self.clock))

                self.willy.moving()
                self.willy.update()

                for j in self.ghosts:
                    for i in self.bullets:
                        i.hit(j)
                    is_living = j.update((self.willy.x, self.willy.y))
                    if not is_living:
                        count += 1
                        self.ghosts.append(Ghost(*self.coords_for_ghosts[random.randint(0, 3)],
                                                 self.ghosts, self.willy, self.clock, 350))
                for i in self.bullets:
                    i.update()

                self.screen.blit(self.bg, (0, 0))
                self.screen.blit(self.willy.image, self.willy.rect)

                # ---------------------------------------
                for wall in self.wall:
                    for i in self.bullets:
                        i.hit(wall)
                for i in range(7):
                    self.screen.blit(self.wall[i].image, self.wall[i].rect)
                # ----------------

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
        if self.willy.HP > 0 and running == True:
            you_win("data/images/game_win1.jpg")
            sl = SecondLevel()
            sl.play()
        elif running == True:
            game_lose()


class SecondLevel:
    def __init__(self, pos_willy=(400, 400), hp_willy=1400, hp_boss=2000):
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
        self.willy = Willy(*pos_willy, [], self.clock, hp_willy)
        self.boss = Boss(hp_boss)

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
                    res = pause(self.willy, [self.boss], 0)
                    print("pause =", res)
                    if not res:
                        print("STOP")
                        running = False
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

                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    # Выстрел игрока
                    self.willy_bullets.append(Bullet((self.willy.x, self.willy.y),
                                                     event.pos, self.willy_bullets, self.clock))
            # Автоматический выстрел босса
            if int(clock) + 1 == int(time.time()):
                self.boss_bullets.append(Boss_bullet((self.boss.x + 130, self.boss.y + 190),
                                                (self.willy.x, self.willy.y), self.boss_bullets,
                                                self.clock))
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
        if self.boss.HP <= 0:
            you_win("data/images/game_win.jpg")
