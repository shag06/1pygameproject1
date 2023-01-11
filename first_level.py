import os, sys, pygame


class Willy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        surf = load_image('face0.png')
        self.image = pygame.transform.scale(surf, (82, 100))
        self.x = x
        self.y = y
        self.speed = 5
        self.rect = self.image.get_rect(topleft=(x, y))

        self.images_face = [f'face{i}.png' for i in range(4)]
        self.images_back = [f'back{i}.png' for i in range(4)]
        self.images_left = [f'left{i}.png' for i in range(4)]
        self.images_right = [f'right{i}.png' for i in range(4)]

        self.move_forward = False
        self.counter_w = 0

        self.move_backwards = False
        self.counter_s = 0

        self.move_left = False
        self.counter_a = 0

        self.move_right = False
        self.counter_d = 0

    def update(self, *args):
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def moving(self):
        if self.move_forward:
            self.image = pygame.transform.scale(load_image(self.images_back[self.counter_w]), (82, 100))
            self.counter_w = (self.counter_w + 1) % 4
            if self.y <= self.speed:
                self.y = 0
            else:
                self.y -= self.speed
        if self.move_backwards:
            self.image = pygame.transform.scale(load_image(self.images_face[self.counter_s]), (82, 100))
            self.counter_s = (self.counter_s + 1) % 4
            if self.y + 100 >= 800 - self.speed:
                self.y = 700
            else:
                self.y += self.speed
        if self.move_left:
            self.image = pygame.transform.scale(load_image(self.images_left[self.counter_a]), (82, 100))
            self.counter_a = (self.counter_a + 1) % 4
            if self.x <= self.speed:
                self.x = 0
            else:
                self.x -= self.speed
        if self.move_right:
            self.image = pygame.transform.scale(load_image(self.images_right[self.counter_d]), (82, 100))
            self.counter_d = (self.counter_d + 1) % 4
            if self.x + 82 >= 1000 - self.speed:
                self.x = 918
            else:
                self.x += self.speed


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, target):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(load_image('bullet.png'), (40, 40))
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.target = target
        self.speed = 5

        self.rect = self.image.get_rect(topleft=pos)

    def update(self, *args):
        # катеты
        if self.pos[1] == self.target[1]:
            if self.pos[0] >= self.target[0]:
                self.x -= self.speed
            else:
                self.x += self.speed
        else:
            tg = abs((self.target[0] - self.pos[0]) / (self.target[1] - self.pos[1]))
            b = ((self.speed / (1 + tg ** 2)) ** 0.5)
            a = ((self.speed / (1 + tg ** 2)) ** 0.5) * tg
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


def load_image(name, colorkey=pygame.Color("WHITE")):
    fullname = os.path.join('', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname).convert()
    image.set_colorkey(colorkey)
    return image


def start_level():
    pygame.init()
    pygame.display.set_caption("Свой курсор мыши")
    size = width, height = 1000, 800
    screen = pygame.display.set_mode(size)
    bg = load_image('ScaledBG.png')
    screen.blit(bg, (0, 0))
    bullets = []
    running = True
    willy = Willy(400, 400)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    willy.move_left = True
                elif event.key == pygame.K_d:
                    willy.move_right = True
                elif event.key == pygame.K_w:
                    willy.move_forward = True
                elif event.key == pygame.K_s:
                    willy.move_backwards = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    willy.move_left = False
                elif event.key == pygame.K_d:
                    willy.move_right = False
                elif event.key == pygame.K_w:
                    willy.move_forward = False
                elif event.key == pygame.K_s:
                    willy.move_backwards = False

            if event.type == pygame.MOUSEBUTTONUP:
                bullets.append(Bullet((willy.x, willy.y), event.pos))

            willy.moving()
            willy.update()

        for i in bullets:
            i.update()

        screen.blit(bg, (0, 0))
        screen.blit(willy.image, willy.rect)
        for bullet in bullets:
            screen.blit(bullet.image, bullet.rect)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    start_level()