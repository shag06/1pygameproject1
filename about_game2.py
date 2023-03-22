import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 800))
screen.fill((255, 255, 255))
pygame.display.set_caption("No peace for Willy!")
main_font = pygame.font.SysFont("cambria", 30)

color_black = (0, 0, 0)
color_white = (255, 255, 255)

font = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 23)

text = font.render('Вас приветствуют разработчики игры!', False, color_black)
text_x = 30
text_y = 10

text2 = font2.render('Как вы заметили на главном экране игры есть три кнопки: "Новая игра", "Загрузить игру", '
                     '"Об игре".', False, color_black)
text2_x = 30
text2_y = 40

text3 = font2.render('При нажатии на "Новая игра" у Вас будет создаваться игра.', False, color_black)
text3_x = 30
text3_y = 60

text4 = font2.render('При нажатии "Загрузить игру" у Вам будет предлагаться выбор игры, которую хотите загрузить',
                     False, color_black)
text4_x = 30
text4_y = 80

text5 = font2.render('Сейчас вы находитесь в "Об игре"', False, color_black)
text5_x = 30
text5_y = 100

text6 = font2.render('При создании новой игры, вы будете оказываться в комнате со стенками, где на вашего персонажа '
                     'пойдут привидения.', False, color_black)
text6_x = 30
text6_y = 150

text7 = font2.render('Приведения наносят урон при соприкосновении с игроком.', False, color_black)
text7_x = 30
text7_y = 170

text8 = font2.render('При соприкосновении со стенками, вы будете от них отталкиваться.', False, color_black)
text8_x = 30
text8_y = 190

text9 = font2.render(
    'Чтобы стрелять нажмите левую кнопку мыши, наведя курсор на приведение (можно в сторону призрака).', False,
    color_black)
text9_x = 30
text9_y = 210

text10 = font2.render('Для хотьбы есть кнопки: "A" - влево, "S" - вниз, "W" - вверх, "D" - вправо.', False, color_black)
text10_x = 30
text10_y = 230

text11 = font2.render('Когда вы убьёте всех привидений, то вы попадёте на 2-ой уровень - игру с боссом. ', False,
                      color_black)
text11_x = 30
text11_y = 290

text12 = font2.render('Теперь урон будет наносится от пуль босса.', False, color_black)
text12_x = 30
text12_y = 310

text13 = font2.render('Ваша задача - уворачиваться от них и стрелять по боссу.', False, color_black)
text13_x = 30
text13_y = 330

text14 = font.render('Удачи Вам!', False, color_black)
text14_x = 30
text14_y = 390

text15 = font2.render('P.S. Если вам понравилась игра, то можете поддержать авторов переводом по номеру 89175647735',
                      False, color_black)
text15_x = 30
text15_y = 450


def about_games():
    running = True
    while running:
        screen.fill(color_white)
        screen.blit(text, (text_x, text_y))
        screen.blit(text2, (text2_x, text2_y))
        screen.blit(text3, (text3_x, text3_y))
        screen.blit(text4, (text4_x, text4_y))
        screen.blit(text5, (text5_x, text5_y))
        screen.blit(text6, (text6_x, text6_y))
        screen.blit(text7, (text7_x, text7_y))
        screen.blit(text8, (text8_x, text8_y))
        screen.blit(text9, (text9_x, text9_y))
        screen.blit(text10, (text10_x, text10_y))
        screen.blit(text11, (text11_x, text11_y))
        screen.blit(text12, (text12_x, text12_y))
        screen.blit(text13, (text13_x, text13_y))
        screen.blit(text14, (text14_x, text14_y))
        screen.blit(text15, (text15_x, text15_y))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
                break
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()


if __name__ == "__main__":
    about_games()
