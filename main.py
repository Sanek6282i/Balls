import pygame
import logic

size = 600, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Balls")
RADIUS_BALL = 20
COLORS = {
    0: (0, 255, 0),
    1: (0, 0, 255),
    2: (255, 0, 0),
    3: (255, 255, 255),
}


def draw_balls(mas):
    """Отрисовка игрового поля"""
    for string in range(1, len(mas[0]) + 1):
        for column in range(1, len(mas) + 1):
            x = 2 * RADIUS_BALL * column + RADIUS_BALL
            y = 2 * RADIUS_BALL * string + RADIUS_BALL
            pygame.draw.circle(screen, COLORS[mas[column][string]], (x, y), RADIUS_BALL)


mas = logic.creation_mas(size[0] // (2 * RADIUS_BALL), size[1] // (2 * RADIUS_BALL))
print(*mas, sep="\n")


# цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            print(f"{x_mouse} {y_mouse}")
            col = x_mouse // (2 * RADIUS_BALL)
            row = y_mouse // (2 * RADIUS_BALL)
        draw_balls(mas)
    pygame.display.update()
