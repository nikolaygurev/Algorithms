"""Задача: наибольший общий делитель

По данным двум числам 1 ≤ a, b ≤ 2 * 10^9 найдите их наибольший общий делитель.

Sample Input 1:
18 35
Sample Output 1:
1

Sample Input 2:
14159572 63967072
Sample Output 2:
4
"""

from math import gcd as gcd_standard


def gcd_iterative(a, b):
    while a:
        a, b = b % a, a
    return b


def gcd_recursive(a, b):
    return gcd_recursive(b % a, a) if a else b


def main():
    a, b = (int(i) for i in input().split())

    print(gcd_iterative(a, b))
    # print(gcd_recursive(a, b))
    # print(gcd_standard(a, b))


if __name__ == '__main__':
    main()
