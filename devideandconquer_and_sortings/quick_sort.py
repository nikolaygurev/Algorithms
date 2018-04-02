from random import randint


def quick_sort(list_to_sort, left_index, right_index):
    """Average time complexity: O(n * log(n))
    Worst time complexity: O(n^2), where n = right_index - left_index
    """
    if left_index < right_index:
        pivot_index = randint(left_index, right_index)  # randomized pivot
        list_to_sort[left_index], list_to_sort[pivot_index] = list_to_sort[pivot_index], list_to_sort[left_index]

        pivot_true_index = partition(list_to_sort, left_index, right_index)

        quick_sort(list_to_sort, left_index, pivot_true_index - 1)
        quick_sort(list_to_sort, pivot_true_index + 1, right_index)


def partition(list_to_sort, left_index, right_index):
    """Time complexity: O(n), where n = right_index - left_index"""
    pivot = list_to_sort[left_index]
    pivot_index = left_index

    for i in range(left_index + 1, right_index + 1):
        if list_to_sort[i] <= pivot:
            pivot_index += 1
            list_to_sort[i], list_to_sort[pivot_index] = list_to_sort[pivot_index], list_to_sort[i]

    # swap pivot to it's correct place
    list_to_sort[left_index], list_to_sort[pivot_index] = list_to_sort[pivot_index], list_to_sort[left_index]
    return pivot_index


def quick_sort_optimized_tail(list_to_sort, left_index, right_index):
    """Average time complexity: O(n * log(n))
    Worst time complexity: O(n^2), where n = right_index - left_index

    Quick sort tail call elimination
    Maximum recursion depth: O(log(n)) while the classic algorithm has O(n)
    """
    while left_index < right_index:
        pivot_index = randint(left_index, right_index)  # randomized pivot
        list_to_sort[left_index], list_to_sort[pivot_index] = list_to_sort[pivot_index], list_to_sort[left_index]

        pivot_true_index = partition(list_to_sort, left_index, right_index)

        # the left list is shorter than the right one
        if (pivot_true_index - left_index) < (right_index - pivot_true_index):
            quick_sort_optimized_tail(list_to_sort, left_index, pivot_true_index - 1)
            left_index = pivot_true_index + 1  # right recursion call elimination

        # the left list isn't shorter than the right one
        else:
            quick_sort_optimized_tail(list_to_sort, pivot_true_index + 1, right_index)
            right_index = pivot_true_index - 1  # left recursion call elimination


def quick_sort_3_way(list_to_sort, left_index, right_index):
    """Average time complexity: O(n * log(n))
    Worst time complexity: O(n^2), where n = right_index - left_index

    Quick sort 3-way partition
    The more identical elements are in the list, the faster this algorithm works compared to the quick_sort
    """
    if left_index < right_index:
        pivot_index = randint(left_index, right_index)  # randomized pivot
        list_to_sort[left_index], list_to_sort[pivot_index] = list_to_sort[pivot_index], list_to_sort[left_index]

        pivot_left_index, pivot_right_index = partition_3_way(list_to_sort, left_index, right_index)
        # j: (pivot_left_index <= j <= pivot_right_index) => list[j] == pivot

        quick_sort_3_way(list_to_sort, left_index, pivot_left_index - 1)
        quick_sort_3_way(list_to_sort, pivot_right_index + 1, right_index)


def partition_3_way(list_to_sort, left_index, right_index):
    """Time complexity: O(n), where n = right_index - left_index"""
    pivot = list_to_sort[left_index]

    pivot_left_index, i = left_index, left_index
    pivot_right_index = right_index

    while i <= pivot_right_index:
        if list_to_sort[i] < pivot:
            list_to_sort[pivot_left_index], list_to_sort[i] = list_to_sort[i], list_to_sort[pivot_left_index]
            pivot_left_index += 1

        elif list_to_sort[i] > pivot:
            list_to_sort[pivot_right_index], list_to_sort[i] = list_to_sort[i], list_to_sort[pivot_right_index]
            pivot_right_index -= 1
            i -= 1  # remain in the same i for the next iteration

        i += 1

    # j: (pivot_left_index <= j <= pivot_right_index) => list[j] == pivot
    return pivot_left_index, pivot_right_index
