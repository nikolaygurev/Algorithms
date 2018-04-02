"""Задача: разбиение множества чисел

Необходимо определить, можно ли данное множество положительных целых чисел разбить на два
подмножества так, что сумма чисел в первом подмножестве равна сумме чисел во втором
подмножестве.
"""

# from rcviz import viz


def find_partition(array):
    """Time complexity: O(k * n), where k = sum(array), n = len(array)"""
    array_sum = sum(array)
    if array_sum % 2 != 0:
        return False

    cache = [([True] + [None] * (array_sum // 2)) for _ in range(len(array) + 1)]
    for j in range(1, array_sum // 2 + 1):
        cache[0][j] = False

    # @viz
    def is_subset_with_sum(arr, n, s):
        """Returns True if there is a subset of arr[:n] with sum equal to s"""
        if cache[n][s] is None:
            if arr[n - 1] > s:  # if last element is greater than sum, then ignore it
                cache[n][s] = is_subset_with_sum(arr, n - 1, s)
            else:
                cache[n][s] = is_subset_with_sum(arr, n - 1, s) or is_subset_with_sum(arr, n - 1, s - arr[n - 1])
        return cache[n][s]

    answer = is_subset_with_sum(array, len(array), array_sum // 2)
    return answer


def main():
    array = [int(i) for i in input().split()]
    print(find_partition(array))


if __name__ == '__main__':
    main()
