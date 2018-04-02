"""Задача: расстояние редактирования

Вычислите расстояние редактирования двух данных непустых строк длины не более 10^2,
содержащих строчные буквы латинского алфавита.

Sample Input 1:
ab
ab
Sample Output 1:
0

Sample Input 2:
short
ports
Sample Output 2:
3
"""


def levenshtein_distance(s1, s2):
    """Time complexity: O(m * n), where m = len(s1), n = len(s2)"""
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    # s1 is always longer than s2

    m, n = len(s1), len(s2)
    previous = list(range(n + 1))

    for i, ch1 in enumerate(s1, 1):
        current = [i]

        for j, ch2 in enumerate(s2, 1):
            current.append(min(current[j - 1] + 1, previous[j] + 1, previous[j - 1] + int(ch1 != ch2)))
        previous = current[:]

    return previous[-1]


def main():
    s1, s2 = input(), input()
    print(levenshtein_distance(s1, s2))


if __name__ == '__main__':
    main()
