"""Задача: огромное число Фибоначчи по модулю

Даны целые числа 1 ≤ n ≤ 10^18 и 2 ≤ m ≤ 10^5, необходимо найти остаток от деления n-го
числа Фибоначчи на m.

Sample Input:
10 2
Sample Output:
1
"""


def large_fib_number_mod(n, m):
    fib_list_mod = [0, 1]

    for i in range(2, n + 1):
        fib_list_mod.append((fib_list_mod[i - 1] + fib_list_mod[i - 2]) % m)

        # two consecutive numbers determine the whole further subsequence
        if (fib_list_mod[i - 1] == 0) and (fib_list_mod[i] == 1):
            fib_list_mod = fib_list_mod[:-2]
            break

    return fib_list_mod[n % len(fib_list_mod)]


def main():
    n, m = (int(i) for i in input().split())
    print(large_fib_number_mod(n, m))


if __name__ == '__main__':
    main()
