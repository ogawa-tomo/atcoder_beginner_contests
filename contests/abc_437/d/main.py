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


N, M = map(int, input().split())
mod = 998244353
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)

cum_sum_A = CumulativeSum(A)
# print(cum_sum_A.range_sum(0, 0))

answer = 0
for b in B:
    ok = -1
    ng = N
    while (ng - ok) > 1:
        mid = (ng + ok) // 2
        if A[mid] >= b:
            ok = mid
        else:
            ng = mid

    # ok: a>bとなる最大のAのインデックス

    if ok >= 0:
        answer += cum_sum_A.range_sum(0, ok) - b * (ok + 1)
        answer %= mod
    if ok < N - 1:
        num = N - 1 - ok
        answer += b * num - cum_sum_A.range_sum(ok + 1, N - 1)
        answer %= mod
print(answer)
