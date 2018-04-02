"""Задача: кодирование Хаффмана

По данной непустой строке s длины не более 10^4, состоящей из строчных букв латинского
алфавита, постройте оптимальный беспрефиксный код. В первой строке выведите количество
различных букв k, встречающихся в строке, и размер получившейся закодированной строки.
В следующих k строках запишите коды букв в формате "letter: code". В последней строке
выведите закодированную строку.

Sample Input 1:
a
Sample Output 1:
1 1
a: 0
0

Sample Input 2:
abacabad
Sample Output 2:
4 14
a: 0
b: 10
c: 110
d: 111
01001100100111
"""

from collections import Counter, namedtuple
import heapq


class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, encoding, binary_code):
        self.left.walk(encoding, binary_code + '0')  # left child's code is appended with 0
        self.right.walk(encoding, binary_code + '1')  # right child's code is appended with 1


class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, encoding, binary_code):
        # if there is only one type of characters in the string, it is encoded by zero
        encoding[self.char] = binary_code or '0'  # every character is encoded by recursively accumulated binary code


def huffman_encoding_v1(s):
    encoding_dict = {}
    heap = [(freq, char) for char, freq in Counter(s).items()]
    heapq.heapify(heap)

    if len(heap) == 1:  # there is only one type of characters in the string
        _freq, char = heapq.heappop(heap)
        encoding_dict[char] = str(0)  # the only type of characters is encoded by zero

    while len(heap) >= 2:  # there are at least two type of characters in the string
        min_freq, min_char = heapq.heappop(heap)
        min2_freq, min2_char = heapq.heappop(heap)

        # (min_char + min2_char) - new nodes accumulate information about their descendants
        heapq.heappush(heap, (min_freq + min2_freq, min_char + min2_char))

        for i, char_string in enumerate([min_char, min2_char]):  # 0 for min_char, 1 for min2_char
            for char in char_string:  # every descendant's code is prepended with 0/1
                if char in encoding_dict:
                    encoding_dict[char] = str(i) + encoding_dict[char]
                else:
                    encoding_dict[char] = str(i)

    return encoding_dict


def huffman_encoding_v2(s):
    heap = []
    for char, freq in Counter(s).items():
        heap.append((freq, len(heap), Leaf(char)))  # len(heap) is used for correct elements comparison

    heapq.heapify(heap)  # second element of every heap element is unique
    count = len(heap)

    while len(heap) >= 2:  # there are at least two type of characters in the string
        min_freq, _min_count, left = heapq.heappop(heap)
        min2_freq, _min2_count, right = heapq.heappop(heap)

        # Node(left, right) - new nodes accumulate information about their descendants
        heapq.heappush(heap, (min_freq + min2_freq, count, Node(left, right)))
        count += 1  # second element of every heap element is unique

    encoding_dict = {}
    if heap:  # if the heap was not empty after creation, at this moment it contains exactly one element
        [(_freq, _count, root)] = heap
        root.walk(encoding_dict, '')  # recursive walk of the entire tree

    return encoding_dict


def main():
    s = input()

    encoding_dict = huffman_encoding_v1(s)
    # encoding_dict = huffman_encoding_v2(s)

    encoded_str = ''.join([encoding_dict[char] for char in s])

    print(len(encoding_dict), len(encoded_str))
    for key, value in sorted(encoding_dict.items()):
        print('{}: {}'.format(key, value))
    print(encoded_str)


if __name__ == '__main__':
    main()
