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


N, Q = map(int, input().split())
A = list(map(int, input().split()))

cum_sum_list: list[int] = []
total = 0
for a in A:
    total += a
    cum_sum_list.append(total)
# print(cum_sum_list)
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        x = q[1]
        x -= 1
        diff = A[x] - A[x + 1]
        A[x] -= diff
        A[x + 1] += diff
        cum_sum_list[x] -= diff
        # print(cum_sum_list)
    elif q[0] == 2:
        l = q[1]
        r = q[2]
        l -= 1
        r -= 1
        if l == 0:
            print(cum_sum_list[r])
        else:
            print(cum_sum_list[r] - cum_sum_list[l - 1])
