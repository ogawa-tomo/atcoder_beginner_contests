# WA
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

zeros = 0
for a in A:
    if a == 0:
        zeros += 1

cum_sum = CumulativeSum(A)

left = 0
right = 0
answer = zeros
while left < N and right < N:
    # print(left, right)
    if A[right] == 0:
        right += 1
        left = right
        continue
    if A[left] == 0:
        left += 1
        if right < left:
            right = left
        continue
    value = cum_sum.range_sum(left, right)
    # print(value)
    if value > K:
        left += 1
        continue
    if value % K == 0:
        # print("^answer")
        answer += 1
        right += 1
        left = right
        continue

    while right < N and cum_sum.range_sum(left, right) < K:
        if A[right] == 0:
            break
        right += 1


print(answer)
