import math


class CumulativeSum:
    def __init__(self, _list: list[int]):
        self._list = _list
        self.length = len(_list)
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
        if left_index < 0 or self.length <= right_index or right_index < left_index:
            raise
        return self.sum(right_index) - self.sum(left_index - 1)


N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 998244353

cum_sum = CumulativeSum(A)

answer = 0
for a in A:
    answer += a**2
    answer %= MOD
answer *= math.comb(N - 1, K - 1)
answer %= MOD

add = 0
if K >= 2:
    for i in range(N - 1):
        add += A[i] * cum_sum.range_sum(i + 1, N - 1)
        add %= MOD
    add *= 2 * math.comb(N - 2, K - 2)
    add %= MOD

answer += add
answer %= MOD
print(answer)
