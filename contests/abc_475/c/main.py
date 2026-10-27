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


N, S, L = map(int, input().split())
A = list(map(int, input().split()))

S -= 1
cum_sum = CumulativeSum(A)

answer = 1

# 左に行って、右にいく
for first in range(S):
    first_trip = cum_sum.range_sum(first, S - 1)
    if first_trip > L:
        continue

    visited = S - first + 1
    answer = max(answer, visited)

    first_trip *= 2
    if first_trip > L:
        continue

    ok = S - 1
    ng = N - 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        second_trip = cum_sum.range_sum(S, mid)
        if first_trip + second_trip <= L:
            ok = mid
        else:
            ng = mid

    arrived = ok
    if S <= arrived:
        visited += arrived - S + 1

    # print(first, arrived, visited)

    answer = max(answer, visited)

# 右に行って、左に行く
for first in range(S, N - 1):
    first_trip = cum_sum.range_sum(S, first)
    if first_trip > L:
        continue

    visited = first - S + 2
    answer = max(answer, visited)

    first_trip *= 2
    if first_trip > L:
        continue

    ok = S
    ng = -1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        second_trip = cum_sum.range_sum(mid, S - 1)
        if first_trip + second_trip <= L:
            ok = mid
        else:
            ng = mid
    arrived = ok
    if arrived < S:
        visited += S - arrived

    answer = max(answer, visited)

print(answer)
