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
for left in range(0, S + 1):
    if left < S:
        left_trip = cum_sum.range_sum(left, S - 1)
    else:
        left_trip = 0

    for right in range(S - 1, N):
        if right > S:
            right_trip = cum_sum.range_sum(S, right - 1)
        else:
            right_trip = 0

        trip = min(left_trip * 2 + right_trip, left_trip + right_trip * 2)
        if trip > L:
            continue

        visited = right - left + 1
        answer = max(answer, visited)

print(answer)
