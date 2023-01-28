import os
import pygame
import sys


# Класс главного персонажа
class Willy(pygame.sprite.Sprite):
    # Инициализация
    def __init__(self, x, y, clock):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        # Скорость движения
        self.speed = 0.5
        # Параметр для анимации движения
        self.LENGTH = 4
        self.HP = 1400

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
            sys.exit()

    # Функция движения
    def moving(self):
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
        self.SPEED = 1
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
    def __init__(self, x, y, group, willy, clock):
        pygame.sprite.Sprite.__init__(self)
        self.pos = (x, y)
        self.speed = 0.02
        self.HP = 350
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
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 300
        self.y = 0

        self.HP = 1000

        image = load_image('data/images/newbullet.png')
        self.image = pygame.transform.scale(image, (300, 200))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update(self):
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        if self.HP <= 0:
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
