def my_sort(list_to_sort):
    return sorted(list_to_sort)


def test(n_iter=1000):
    from random import randint

    for _ in range(n_iter):
        length = randint(0, 10 ** 3)
        list_to_sort = [randint(-10 ** 3, 10 ** 3) for _ in range(length)]

        try:
            assert sorted(list_to_sort) == my_sort(list_to_sort)
        except AssertionError:
            print(list_to_sort, sorted(list_to_sort), my_sort(list_to_sort), sep='\n')
            break
    print('Success!')


def main():
    list_to_sort = [int(i) for i in input().split()]
    print(my_sort(list_to_sort))


if __name__ == '__main__':
    main()
