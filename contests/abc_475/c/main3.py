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


N, S, L = map(int, input().split())
A = list(map(int, input().split()))

S -= 1

cum_sum = CumulativeSum(A)


def get_distance(left, right):
    if left == right:
        return 0
    return cum_sum.range_sum(left, right - 1)


answer = 1

# 左に行ってから右に行く
for left in range(0, S + 1):
    first_trip = get_distance(left, S)
    if first_trip > L:
        continue
    visited = S - left + 1
    answer = max(answer, visited)
    first_trip *= 2
    if first_trip > L:
        continue
    for right in range(S, N):
        second_trip = get_distance(S, right)
        distance = first_trip + second_trip
        if distance <= L:
            answer = max(answer, right - left + 1)

# 右に行ってから左に行く
for right in range(S, N):
    first_trip = get_distance(S, right)
    if first_trip > L:
        continue
    visited = right - S + 1
    answer = max(answer, visited)
    first_trip *= 2
    if first_trip > L:
        continue
    for left in range(0, S + 1):
        second_trip = get_distance(left, S)
        distance = first_trip + second_trip
        if distance <= L:
            answer = max(answer, right - left + 1)

print(answer)
