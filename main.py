import pygame
pygame.init()
from random import randrange


class Balls:

    col, row = (10, 15)  # количество столбцов и строк на игровом поле
    RADIUS_BALL = 30
    screen = pygame.display.set_mode((col * 2 * RADIUS_BALL, row * 2 * RADIUS_BALL))
    pygame.display.set_caption("Balls")

    COLORS = {
        1: (0, 255, 0),
        2: (0, 0, 255),
        3: (255, 0, 0),
        4: (255, 255, 255),
    }

    def __init__(self):
        self.group_balls = []  # Массив для хранения одинаковых шаров рядом
        self.mas = []  # Массив шаров
        """Создание массива заполненого 0 повернутого на 90 градусов для простоты модификации массива.
         размер col x row  с добавлением краевых значений для предотвращения выхода за пределы массива"""
        for i in range(Balls.col + 2):  # Колонки
            temp = []
            for j in range(Balls.row + 2):  # строки
                temp.append(0)
            self.mas.append(temp)

    def __created_random_balls(self):
        """заполняет массив рандомными значениями обозначающими цвет шара"""
        # # self.mas = [
        #     [0, 0, 0, 0, 0, 0],
        #     [0, 3, 1, 1, 2, 0],
        #     [0, 2, 3, 3, 2, 0],
        #     [0, 4, 3, 4, 1, 0],
        #     [0, 4, 2, 3, 2, 0],
        #     [0, 2, 2, 3, 4, 0],
        #     [0, 4, 3, 3, 4, 0],
        #     [0, 2, 3, 2, 2, 0],
        #     [0, 0, 0, 0, 0, 0]
        # ]

        for i in range(1, Balls.col + 1):  # колонки
            for j in range(1, Balls.row + 1):  # строки
                if self.mas[i][j] == 0:
                    self.mas[i][j] = randrange(1, 5)
                else:
                    break

    def __check_mas(self, c=-1, r=-1):
        '''Проверка и нахождение групп шаров >= 3.
        Еесли не передана позиция шара, ищет есть ли вообще хоть одна группа шаров >= 3
        '''
        if c != -1 and r != -1:
            self.__search_same_nearby(c, r)
            print(self.group_balls)
            if len(self.group_balls) >= 3:
                return True
            self.group_balls.clear()
            return False
        else:
            for i in range(1, Balls.col + 1):  # колонки
                for j in range(1, Balls.row + 1):  # строки
                    if len(self.__check_mas(i, j)) >= 3:
                        self.group_balls.clear()
                        return True
            self.group_balls.clear()
            return False

    @staticmethod
    def __get_number_from_index(c, r):
        return (r - 1) * Balls.row + c

    @staticmethod
    def __get_index_from_number(num):
        num -= 1
        r = num // Balls.row + 1
        c = num - (r - 1) * Balls.row + 1
        print("index ", c, r)
        return c, r

    def __del_group_balls(self):
        self.group_balls.sort()
        print(self.group_balls)
        while self.group_balls:
            print(self.group_balls)
            cd, rd = self.__get_index_from_number(self.group_balls.pop())
            print(cd, rd, self.__get_number_from_index(cd, rd))
            del self.mas[rd][cd]

    def __filling_mas(self):
        for i in range(Balls.col + 2):
            len_line = len(self.mas[i])
            if len_line < Balls.row + 2:
                self.mas[i] = ([0] * (Balls.row + 2 - len_line)) + self.mas[i]

    def __search_same_nearby(self, c, r):
        """Поиск одинаоквых шаров рядом по вертикали и горизонтали"""
        if self.__get_number_from_index(c, r) not in self.group_balls:
            self.group_balls.append(self.__get_number_from_index(c, r))
            if self.mas[r][c] == self.mas[r][c - 1]:
                self.__search_same_nearby(c - 1, r)
            if self.mas[r][c] == self.mas[r][c + 1]:
                self.__search_same_nearby(c + 1, r)
            if self.mas[r][c] == self.mas[r - 1][c]:
                self.__search_same_nearby(c, r - 1)
            if self.mas[r][c] == self.mas[r + 1][c]:
                self.__search_same_nearby(c, r + 1)

    def __draw_balls(self):
        """Отрисовка игрового поля c правильным расположением массива"""
        for i in range(1, Balls.row + 1):
            for j in range(1, Balls.col + 1):
                x = 2 * Balls.RADIUS_BALL * (j - 1) + Balls.RADIUS_BALL
                y = 2 * Balls.RADIUS_BALL * (i - 1) + Balls.RADIUS_BALL
                pygame.draw.circle(Balls.screen, Balls.COLORS[self.mas[j][i]], (x, y), Balls.RADIUS_BALL)

    def __draw_numbers(self):
        font = pygame.font.SysFont('ubuntu', 30)
        counter = 1
        for j in range(1, Balls.col + 1):
            for i in range(1, Balls.row + 1):
                text = font.render(f"{counter}", True, (0, 0, 0))
                x = 2 * Balls.RADIUS_BALL * (j - 1) + Balls.RADIUS_BALL
                y = 2 * Balls.RADIUS_BALL * (i - 1) + Balls.RADIUS_BALL
                font_w, font_h = text.get_size()
                text_x = x - font_w / 2
                text_y = y - font_h / 2
                Balls.screen.blit(text, (text_x, text_y))
                counter += 1

    def __print_mas(self):
        for i in self.mas:
            print(*i)
        print()
        for j in range(1, Balls.row + 1):
            for i in range(1, Balls.col + 1):
                print(self.mas[i][j], end=" ")
            print()

    def start_game(self):
        """Запуск цикла игры"""
        self.__created_random_balls()
        self.__print_mas()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # закрытие окна на крестик
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:  # Нажатие  на шар
                    x_mouse, y_mouse = pygame.mouse.get_pos()
                    print(f"x = {x_mouse} y = {y_mouse}")
                    col_mouse = x_mouse // (2 * Balls.RADIUS_BALL)
                    row_mouse = y_mouse // (2 * Balls.RADIUS_BALL)
                    print(f"x = {col_mouse} y = {row_mouse} - {col_mouse * Balls.row + row_mouse + 1}")
                    if self.__check_mas(row_mouse + 1, col_mouse + 1):
                        self.__del_group_balls()
                        self.__filling_mas()
                        self.__created_random_balls()
                self.__draw_balls()
                self.__draw_numbers()
            pygame.display.update()


game = Balls()
game.start_game()
