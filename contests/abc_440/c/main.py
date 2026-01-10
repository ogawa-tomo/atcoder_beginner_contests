# WA
from collections import defaultdict


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
    # print(C)
    # C.extend(C)

    mod = 2 * W

    amari = N % mod
    if amari != 0:
        nobasu = mod - amari
        C.extend([0] * nobasu)
    # print(C)
    cum_sum = CumulativeSum(C)

    # if W >= N:
    #     print(0)
    #     continue
    c_length = len(C)

    # costs[m]: m番目のセットのコスト
    costs: list[int] = [0] * mod
    for m in range(min(mod, N)):
        # m番目のコストを計算する
        start = m
        while True:
            end = start + W - 1
            if start >= c_length:
                break
            if end >= c_length:
                # hamide = end - N
                end = end - c_length
                costs[m] += cum_sum.range_sum(start, c_length - 1)
                costs[m] += cum_sum.range_sum(0, end)
                break

            costs[m] += cum_sum.range_sum(start, end)
            start += mod
    # print(costs)
    print(min(costs))
