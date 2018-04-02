"""Задача: небольшое число Фибоначчи

Дано целое число 1 ≤ n ≤ 40, необходимо вычислить n-е число Фибоначчи при n ≥ 2).

Sample Input:
3
Sample Output:
2
"""

# from rcviz import viz
from functools import lru_cache


def fib_iterative(n):
    f0, f1 = 0, 1
    for _ in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1


# @viz
def fib_recursive(n):
    return n if n <= 1 else fib_recursive(n - 1) + fib_recursive(n - 2)


# @viz
@lru_cache(maxsize=None)
def fib_recursive_with_cache(n):
    return n if n <= 1 else fib_recursive_with_cache(n - 1) + fib_recursive_with_cache(n - 2)


def main():
    n = int(input())

    print(fib_iterative(n))
    # print(fib_recursive(n))
    # print(fib_recursive_with_cache(n))


if __name__ == '__main__':
    main()
