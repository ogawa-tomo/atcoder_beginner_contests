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

# leftとrightに行く（どちらが先でもよい）
for left in range(0, S + 1):
    distance_to_left = get_distance(left, S)
    for right in range(S, N):
        distance_to_right = get_distance(S, right)
        distance = min(
            distance_to_left * 2 + distance_to_right,
            distance_to_left + distance_to_right * 2,
        )
        if distance <= L:
            answer = max(answer, right - left + 1)

print(answer)
