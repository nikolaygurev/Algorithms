def insertion_sort(list_to_sort):
    """Time complexity: O(n^2), where n = len(list_to_sort)"""
    for i in range(len(list_to_sort) - 1):
        j = i
        while j >= 0 and list_to_sort[j] > list_to_sort[j + 1]:
            list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
            j -= 1


def selection_sort(list_to_sort):
    """Time complexity: O(n^2), where n = len(list_to_sort)"""
    for i in range(len(list_to_sort) - 1):
        min_i = i
        for j in range(i + 1, len(list_to_sort)):
            if list_to_sort[j] < list_to_sort[min_i]:
                min_i = j
        if min_i != i:
            list_to_sort[i], list_to_sort[min_i] = list_to_sort[min_i], list_to_sort[i]


def bubble_sort(list_to_sort):
    """Time complexity: O(n^2), where n = len(list_to_sort)"""
    for i in range(len(list_to_sort) - 1):
        for j in range(len(list_to_sort) - 1 - i):
            if list_to_sort[j] > list_to_sort[j + 1]:
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
