def merge_sort_recursive(list_to_sort):
    """Time complexity: O(n * log(n)), where n = len(unsorted_list)"""
    if len(list_to_sort) <= 1:
        return list_to_sort

    middle_index = len(list_to_sort) // 2

    left_list = merge_sort_recursive(list_to_sort[:middle_index])
    right_list = merge_sort_recursive(list_to_sort[middle_index:])

    return merge(left_list, right_list)


def merge_sort_iterative(list_to_sort):
    """Time complexity: O(n * log(n)), where n = len(unsorted_list)"""
    if len(list_to_sort) <= 1:
        return list_to_sort

    list_to_sort = [[element] for element in list_to_sort]
    while len(list_to_sort) > 1:
        left_list = list_to_sort[0]
        right_list = list_to_sort[1]
        del list_to_sort[:2]
        list_to_sort.append(merge(left_list, right_list))

    return list_to_sort[0]


def merge(left_list, right_list):
    """Time complexity: O(n), where n = len(left_list) + len(right_list)"""
    merged_list = []
    i, j = 0, 0

    while i < len(left_list) and j < len(right_list):
        if left_list[i] <= right_list[j]:
            merged_list.append(left_list[i])
            i += 1
        else:
            merged_list.append(right_list[j])
            j += 1

    # at least one of the lists (left_list[i:], right_list[j:]) is empty
    merged_list.extend(left_list[i:] + right_list[j:])
    return merged_list
