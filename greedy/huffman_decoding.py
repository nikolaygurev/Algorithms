"""Задача: декодирование Хаффмана

Восстановите строку по её коду и беспрефиксному коду символов.

В первой строке входного файла заданы два целых числа k и l через пробел — количество
различных букв, встречающихся в строке, и размер получившейся закодированной строки,
соответственно. В следующих k строках записаны коды букв в формате "letter: code". Ни один
код не является префиксом другого. Буквы могут быть перечислены в любом порядке. В качестве
букв могут встречаться лишь строчные буквы латинского алфавита; каждая из этих букв
встречается в строке хотя бы один раз. Наконец, в последней строке записана закодированная
строка. Исходная строка и коды всех букв непусты. Заданный код таков, что закодированная
строка имеет минимальный возможный размер.


В первой строке выходного файла выведите строку s. Она должна состоять из строчных букв
латинского алфавита. Гарантируется, что длина правильного ответа не превосходит 10^4 символов.

Sample Input 1:
1 1
a: 0
0
Sample Output 1:
a

Sample Input 2:
4 14
a: 0
b: 10
c: 110
d: 111
01001100100111
Sample Output 2:
abacabad
"""

import random
import string
from huffman_encoding import huffman_encoding_v1, huffman_encoding_v2


def huffman_decoding(encoding_dict, encoded_str):
    decoded_str = ''
    encoding_dict = {value: key for key, value in encoding_dict.items()}

    sequence = ''
    for char in encoded_str:
        sequence += char
        if sequence in encoding_dict:
            decoded_str += encoding_dict[sequence]
            sequence = ''

    return decoded_str


def test(n_iter=1000):
    for _ in range(n_iter):
        length = random.randint(0, 10 ** 4)
        s = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

        encoding_dict1 = huffman_encoding_v1(s)
        encoding_dict2 = huffman_encoding_v2(s)

        encoded_str1 = ''.join([encoding_dict1[char] for char in s])
        encoded_str2 = ''.join([encoding_dict2[char] for char in s])

        decoded_str1 = huffman_decoding(encoding_dict1, encoded_str1)
        decoded_str2 = huffman_decoding(encoding_dict2, encoded_str2)

        assert len(encoded_str1) == len(encoded_str2)
        assert decoded_str1 == decoded_str2 == s

    print('Success!')


def main():
    k, _l = (int(i) for i in input().split())

    encoding_dict = {}
    for _ in range(k):
        key, value = (i.strip() for i in input().split(':'))
        encoding_dict[key] = value

    encoded_str = input()
    print(huffman_decoding(encoding_dict, encoded_str))


if __name__ == '__main__':
    main()
    # test()
