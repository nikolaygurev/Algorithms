"""Задача: очередь с приоритетами

Первая строка входа содержит число операций 1 ≤ n ≤ 10^5. Каждая из последующих n строк
задает операцию одного из следующих двух типов:

Insert x, где 0 ≤ x ≤ 10^9 — целое число;
ExtractMax.

Первая операция добавляет число x в очередь с приоритетами, вторая — извлекает максимальное
число и выводит его.

Sample Input:
6
Insert 200
Insert 10
ExtractMax
Insert 5
Insert 500
ExtractMax
Sample Output:
200
500
"""

import sys
import heapq
import random


class PriorityQueueHandMade:
    queue = []

    def _sift_down(self, i):
        """Time complexity: O(log(n)), where n = len(self.queue)"""
        while 2 * i + 1 < len(self.queue):  # while left child's index < len(queue)
            left_child_index = 2 * i + 1
            right_child_index = 2 * i + 2
            j = left_child_index

            if right_child_index < len(self.queue) and self.queue[right_child_index] > self.queue[left_child_index]:
                j = right_child_index

            if self.queue[i] >= self.queue[j]:  # parent > than both children
                break

            self.queue[j], self.queue[i] = self.queue[i], self.queue[j]  # swap(parent, the largest child)
            i = j  # repeat for the largest child

    def _sift_up(self, i):
        """Time complexity: O(log(n)), where n = len(self.queue)"""
        while self.queue[i] > self.queue[int((i - 1) / 2)]:  # child > parent
            # swap(parent, child)
            self.queue[i], self.queue[int((i - 1) / 2)] = self.queue[int((i - 1) / 2)], self.queue[i]
            i = int((i - 1) / 2)  # repeat for parent; int(-0.5) == 0

    def insert(self, priority):
        """Time complexity: O(log(n)), where n = len(self.queue)"""
        self.queue.append(priority)
        self._sift_up(len(self.queue) - 1)  # sift up of the new element

    def extract_max(self):
        """Time complexity: O(log(n)), where n = len(self.queue)"""
        queue_max = self.queue[0]
        self.queue[0] = self.queue[-1]
        del self.queue[-1]
        self._sift_down(0)  # sift down of the new queue[0] element
        return queue_max


class PriorityQueueStandardLibrary:
    queue = []
    heapq.heapify(queue)

    def insert(self, priority):
        """Time complexity: O(log(n)), where n = len(self.queue)"""
        heapq.heappush(self.queue, -priority)  # (-priority) because it's a min heap

    def extract_max(self):
        """Time complexity: O(log(n)), where n = len(self.queue)"""
        return -heapq.heappop(self.queue)  # minus because every heap element is a negative number


def test(n_iter=100):
    commands_list = ['Insert', 'ExtractMax']

    for i in range(n_iter):
        n = random.randint(1, 10 ** 5)

        priority_queue_hand_made = PriorityQueueHandMade()
        priority_queue_standard_library = PriorityQueueStandardLibrary()

        for _ in range(n):
            line = random.choice(commands_list)

            if line == 'Insert':
                value = random.randint(0, 10 ** 9)

                priority_queue_hand_made.insert(value)
                priority_queue_standard_library.insert(value)

            else:
                len1 = len(priority_queue_hand_made.queue)
                len2 = len(priority_queue_standard_library.queue)

                if (len1 == 0 and len2 != 0) or (len1 != 0 and len2 == 0):
                    raise RuntimeError

                if len1 > 0 and len2 > 0:
                    assert priority_queue_hand_made.extract_max() == priority_queue_standard_library.extract_max()

        print('Successful iteration!')


def main():
    priority_queue = PriorityQueueHandMade()
    # priority_queue = PriorityQueueStandardLibrary()

    n_ = input()
    for line in sys.stdin.readlines():

        if line.startswith('Insert'):
            _command, n = line.split()
            priority_queue.insert(int(n))
        else:
            print(priority_queue.extract_max())


if __name__ == '__main__':
    main()
    # test()
