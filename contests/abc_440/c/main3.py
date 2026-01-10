# AC
import sys


class CumulativeSum:
    def __init__(self, _list: list[int]):
        self._list = _list
        total = 0
        self.cumulative_sum_list: list[int] = []
        for elem in self._list:
            total += elem
            self.cumulative_sum_list.append(total)

    def sum(self, index: int):
        if index == -1:
            return 0
        return self.cumulative_sum_list[index]

    def range_sum(self, left_index: int, right_index: int):
        return self.sum(right_index) - self.sum(left_index - 1)


T = int(input())
for _ in range(T):
    N, W = map(int, input().split())
    C = list(map(int, input().split()))

    mod = 2 * W
    cost_list = [0] * mod

    for i, c in enumerate(C):
        m = i % mod
        cost_list[m] += c
    cost_list *= 2
    cum_sum = CumulativeSum(cost_list)

    # print(cost_list)
    answer = sys.maxsize
    for i in range(mod):
        cost = cum_sum.range_sum(i, i + W - 1)
        answer = min(answer, cost)
    print(answer)
