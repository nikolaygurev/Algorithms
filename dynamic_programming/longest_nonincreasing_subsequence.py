"""Задача: наибольшая невозрастающая подпоследовательность

Дано целое число 1 ≤ n ≤ 10^5 и массив A[1…n], содержащий неотрицательные целые числа, не
превосходящие 10^9. Найдите наибольшую невозрастающую подпоследовательность в A. В первой
строке выведите её длину k, во второй — её индексы 1 ≤ i1 < i2 < … < ik ≤ n (таким образом,
A[i1] ≥ A[i2] ≥ … ≥ A[in]).

Sample Input:
5
5 3 4 4 2
Sample Output:
4
1 3 4 5
"""

from bisect import bisect_right


def longest_non_increasing_subsequence(sequence):
    """Time complexity: O(n * log(n)), where n = len(sequence)"""
    sequence.reverse()  # for decreasing or non-increasing subsequences

    last_numbers = [-float('inf')] + [float('inf')] * len(sequence)
    positions = [-1] * (len(sequence) + 1)
    previous = [-1] * len(sequence)
    length = 0

    for i in range(len(sequence)):
        pos = bisect_right(last_numbers, sequence[i])

        # if last_numbers[pos - 1] < sequence[i]:  # for increasing and decreasing subsequences
        if True:  # for non-increasing or non-decreasing subsequences
            last_numbers[pos] = sequence[i]
            positions[pos] = i
            previous[i] = positions[pos - 1]
            length = max(length, pos)

    # subsequence assembly
    indices = []
    pos = positions[length]
    while pos != -1:
        # indices.append(pos + 1)  # for increasing and non-decreasing subsequences
        indices.append(len(sequence) - pos)  # for decreasing or non-increasing subsequences
        pos = previous[pos]

    # indices.reverse()  # for increasing and non-decreasing subsequences
    return length, indices


def main():
    n_ = input()
    sequence = [int(i) for i in input().split()]

    length, indices = longest_non_increasing_subsequence(sequence)
    print(length)
    print(*indices)  # 1 <= index <= len(sequence) for index in indices


if __name__ == '__main__':
    main()
