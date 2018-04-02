"""Задача: непрерывный рюкзак

Первая строка содержит количество предметов 1 ≤ n ≤ 10^3 и вместимость рюкзака
0 ≤ W ≤ 2 * 10^6. Каждая из следующих n строк задаёт стоимость 0 ≤ ci ≤ 2 * 10^6 и объём
0 < wi ≤ 2 * 10^6 предмета (n, W, ci, wi — целые числа). Выведите максимальную стоимость
частей предметов (от каждого предмета можно отделить любую часть, стоимость и объём при
этом пропорционально уменьшатся), помещающихся в данный рюкзак, с точностью не менее трёх
знаков после запятой.

Sample Input:
3 50
60 20
100 50
120 30
Sample Output:
180.000
"""

import heapq
import sys


def list_continuous_knapsack(capacity, item_list):
    item_list.sort(key=lambda x: x[0] / x[1], reverse=True)

    full_cost = 0

    for cost, weight in item_list:
        if weight < capacity:
            full_cost += cost
            capacity -= weight
        else:
            full_cost += cost / weight * capacity
            break

    return float("{:.3f}".format(full_cost))


def heapified_continuous_knapsack(capacity, item_list):
    item_heap = [(-cost / weight, weight) for cost, weight in item_list]  # (-cost) because is's a min heap
    heapq.heapify(item_heap)

    full_cost = 0

    while item_heap and capacity:
        cost_per_weight, weight = heapq.heappop(item_heap)  # returns the highest value
        weight_reduction = min(weight, capacity)

        full_cost += -cost_per_weight * weight_reduction  # (-cost_per_weight) because it's a negative number
        capacity -= weight_reduction

    return float("{:.3f}".format(full_cost))


def simple_input():
    n, capacity = (int(i) for i in input().split())
    item_list = [(tuple(map(int, input().split()))) for _ in range(n)]

    return capacity, item_list


def advanced_input():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)

    n, capacity = next(reader)
    item_list = list(reader)

    assert len(item_list) == n
    return capacity, item_list


def main():
    # capacity, item_list = simple_input()
    capacity, item_list = advanced_input()

    print(list_continuous_knapsack(capacity, item_list))
    # print(heapified_continuous_knapsack(capacity, item_list))


if __name__ == '__main__':
    main()
