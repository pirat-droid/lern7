'''
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
 который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8
'''
import numpy as np


class Matrix:

    def __init__(self, array):
        self.array = array

    def __add__(self, other):
        return Matrix(self.array + other.array)

    def __str__(self):
        return f'{self.array}'

    def __del__(self):
        pass


if __name__ == '__main__':
    arr_1 = Matrix(np.array([[3,3,3],[2,5,5]]))
    arr_2 = Matrix(np.array([[2,4,2],[1,3,8]]))
    print(arr_1 + arr_2)
