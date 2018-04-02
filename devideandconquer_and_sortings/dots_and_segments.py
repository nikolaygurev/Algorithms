"""Задача: точки и отрезки

В первой строке задано два целых числа 1 ≤ n ≤ 50000 и 1 ≤ m ≤ 50000 — количество отрезков
и точек на прямой, соответственно. Следующие n строк содержат по два целых числа ai и bi
(ai ≤ bi) — координаты концов отрезков. Последняя строка содержит m целых чисел — координаты
точек. Все координаты не превышают 10^8 по модулю. Точка считается принадлежащей отрезку,
если она находится внутри него или на границе. Для каждой точки в порядке появления во вводе
выведите, скольким отрезкам она принадлежит.

Sample Input:
2 3
0 5
7 10
1 6 11
Sample Output:
1 0 0
"""

import sys


def dots_and_segments(bounds_and_dots, dots_count):
    """Time complexity: O(k), where k = len(bounds_and_dots) == 2 * n + m"""
    bounds_and_dots.sort()

    result = [0] * dots_count
    current = 0  # current number of started but not finished segments

    for dot in bounds_and_dots:
        current -= dot[1]
        if dot[1] == 0:
            result[dot[2]] = current

    return result


def input_and_processing(reader):
    """Time complexity: O(n + m)"""
    n, m = next(reader)
    bounds_and_dots = []  # left bounds, right bounds and input dots

    for _ in range(n):
        left, right = next(reader)
        bounds_and_dots.append((left, -1))  # -1 means left bound of the segment
        bounds_and_dots.append((right, 1))  # 1 means left bound of the segment

    input_dots = [int(i) for i in next(reader)]

    for i in range(len(input_dots)):
        bounds_and_dots.append((input_dots[i], 0, i))  # 0 means dot, i saves the order of all input dots

    return bounds_and_dots, m


def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)

    bounds_and_dots, dots_count = input_and_processing(reader)
    print(*dots_and_segments(bounds_and_dots, dots_count))


if __name__ == '__main__':
    main()
