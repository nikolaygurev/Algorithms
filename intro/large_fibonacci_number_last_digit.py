"""Задача: последняя цифра большого числа Фибоначчи

Дано число 1 ≤ n ≤ 10^7, необходимо найти последнюю цифру n-го числа Фибоначчи.

Sample Input:
875577
Sample Output:
2
"""


def large_fib_number_last_digit_iterative(n):
    f0, f1 = 0, 1
    for _ in range(n):
        f0, f1 = f1, (f0 + f1) % 10
    return f0


def large_fib_number_last_digit_arithm(n):
    length = 60  # length of the period of the (Fibonacci numbers mod 10 sequence in range(0, k), k >= 59)
    n %= length

    # Fibonacci numbers formula
    fib_number = int((1 / 5 ** 0.5) * (((1 + 5 ** 0.5) / 2) ** n - ((1 - 5 ** 0.5) / 2) ** n))
    return fib_number % 10


def main():
    n = int(input())

    print(large_fib_number_last_digit_iterative(n))
    # print(large_fib_number_last_digit_arithm(n))


if __name__ == '__main__':
    main()
