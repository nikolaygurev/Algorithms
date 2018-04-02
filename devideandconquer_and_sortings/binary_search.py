"""Задача: двоичный поиск
﻿
В первой строке даны целое число 1 ≤ n ≤ 10^5 и массив A[1…n] из n различных натуральных
чисел, не превышающих 10^9, в порядке возрастания, во второй — целое число 1 ≤ k ≤ 10^5 и
k натуральных чисел b1,…,bk, не превышающих 10^9. Для каждого i от 1 до k необходимо
вывести индекс 1 ≤ j ≤ n, для которого A[j]=bi, или −1, если такого j нет.

Sample Input:
5 1 5 8 12 13
5 8 1 23 1 11
Sample Output:
3 1 -1 1 -1
"""

from bisect import bisect_left
import sys


def binary_search(numbers_list, key):
    """Time complexity: O(log(n)), where n = len(numbers_list)"""
    left_bound = 0
    right_bound = len(numbers_list)
    # Invariant: left_bound <= key_pos < right_bound

    while left_bound < right_bound:
        middle = (left_bound + right_bound) // 2

        if key == numbers_list[middle]:
            return middle + 1
        elif key < numbers_list[middle]:
            right_bound = middle
        else:
            left_bound = middle + 1

    return -1


def binary_search_bisect(numbers_list, key):
    """Time complexity: O(log(n)), where n = len(numbers_list)"""
    left_bound = bisect_left(numbers_list, key)
    # i: (i < left bound) => numbers_list[i] < key

    if left_bound < len(numbers_list) and numbers_list[left_bound] == key:
        return left_bound + 1
    else:
        return -1


def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    n_, *a = next(reader)
    k_, *b = next(reader)

    answers_list = [binary_search(a, number) for number in b]
    # answers_list = [binary_search_bisect(a, number) for number in b]
    print(*answers_list)


if __name__ == '__main__':
    main()
