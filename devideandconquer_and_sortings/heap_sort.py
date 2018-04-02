def heap_sort(list_to_sort):
    """Time complexity: O(n * log(n)), where n = len(list_to_sort)"""
    build_max_heap(list_to_sort)

    for i in range(len(list_to_sort) - 1, 0, -1):
        list_to_sort[i], list_to_sort[0] = list_to_sort[0], list_to_sort[i]
        _sift_down(list_to_sort, 0, i)


def build_max_heap(list_to_sort):
    """Time complexity: O(n), where n = len(list_to_sort)"""
    for i in range(int((len(list_to_sort) - 1) / 2), -1, -1):
        _sift_down(list_to_sort, i, len(list_to_sort))


def _sift_down(heap, i, size):
    """Time complexity: O(log(size))"""
    while 2 * i + 1 < size:  # while left child's index < size
        left_child_index = 2 * i + 1
        right_child_index = 2 * i + 2
        j = left_child_index

        if right_child_index < size and heap[right_child_index] > heap[left_child_index]:
            j = right_child_index

        if heap[i] >= heap[j]:  # parent > than both children
            break

        heap[j], heap[i] = heap[i], heap[j]  # swap(parent, the largest child)
        i = j  # repeat for the largest child
