import random


def creation_mas(col, row):
    """
    Создает массив со случайными значениями, для выбора цвета шара
    :param col: количество столбцов
    :param row: количество строк
    :return:
    """
    mas = [[random.randrange(0, 4) for _ in range(row + 2)] for _ in range(col + 2)]
    return mas



