"""Задача: покрыть отрезки точками

По данным n отрезкам необходимо найти множество точек минимального размера, для которого
каждый из отрезков содержит хотя бы одну из точек.

В первой строке дано число 1 ≤ n ≤ 100 отрезков. Каждая из последующих n строк содержит по
два числа 0 ≤ l ≤ r ≤ 10^9, задающих начало и конец отрезка. Выведите оптимальное число m
точек и сами m точек. Если таких множеств точек несколько, выведите любое из них.

Sample Input 1:
3
1 3
2 5
3 6
Sample Output 1:
1
3

Sample Input 2:
4
4 7
1 3
2 5
5 6
Sample Output 2:
2
3 6
"""


def segments_coating(segments_list):
    segments_list.sort(key=lambda x: x[1])

    dots_list = [segments_list[0][1]]

    for segment in segments_list:
        if segment[0] > dots_list[-1]:
            dots_list.append(segment[1])

    return dots_list


def main():
    segments_list = [list(map(int, input().split())) for _ in range(int(input()))]
    dots_list = segments_coating(segments_list)

    print(len(dots_list))
    print(*dots_list)


if __name__ == '__main__':
    main()
