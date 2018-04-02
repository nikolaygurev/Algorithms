"""Задача: различные слагаемые

По данному числу 1 ≤ n ≤ 10^9 найдите максимальное число k, для которого n можно представить
как сумму k различных натуральных слагаемых. Выведите в первой строке число k, во второй — k
слагаемых.

Sample Input 1:
4
Sample Output 1:
2
1 3

Sample Input 2:
6
Sample Output 2:
3
1 2 3
"""


def different_addends_iterative(n):
    k = 1
    addends = []

    while n >= 2 * k + 1:
        addends.append(k)
        n -= k
        k += 1

    addends.append(n)
    return k, addends


def different_addends_arithm_progr(n):
    k = int((-1 + (1 + 8 * n) ** 0.5) / 2)  # based on theoretical calculations

    addends = list(range(1, k))
    addends.append(n - (k - 1) * k // 2)  # based on theoretical calculations

    return k, addends


def main():
    n = int(input())

    k, addends = different_addends_iterative(n)
    # k, addends = different_addends_arithm_progr(n)

    print(k)
    print(*addends)


if __name__ == '__main__':
    main()
