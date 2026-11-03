from typing import Callable


def most_left_ok(min_i: int, max_i: int, ok_func: Callable[[int], bool]):
    ok = max_i + 1
    ng = min_i - 1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if ok_func(mid):
            ok = mid
        else:
            ng = mid
    if ok > max_i:
        return None
    return ok


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


N = int(input())
S = input()

o_list: list[int] = []
x_list: list[int] = []
for s in S:
    if s == "o":
        o_list.append(1)
        x_list.append(0)
    else:
        o_list.append(0)
        x_list.append(1)

cum_sum_o = CumulativeSum(o_list)
cum_sum_x = CumulativeSum(x_list)

for i in range(N):
    if i == N - 1:
        print(N)
        continue

    atari = cum_sum_o.range_sum(0, i)

    if atari == 0:
        print(i + 1)
        continue

    right = most_left_ok(
        i + 1, N - 1, lambda right: cum_sum_x.range_sum(i + 1, right) >= atari
    )

    if right is None:
        print(N)
        continue

    print(right + 1)
