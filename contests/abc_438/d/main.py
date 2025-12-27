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


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

cum_sum_A = CumulativeSum(A)
cum_sum_B = CumulativeSum(B)
cum_sum_C = CumulativeSum(C)


class BCSplit:
    def __init__(self, b_last_i: int, total: int):
        self.b_last_i = b_last_i  # Bの最後のインデックス
        self.total = total

    def __repr__(self):
        return str((self.b_last_i, self.total))

    def __lt__(self, other):
        return self.total < other.total


bc_splits: list[BCSplit] = []
# BとCを分けたときの合計値を調べる
for i in range(1, N - 1):
    total = cum_sum_B.range_sum(0, i) + cum_sum_C.range_sum(i + 1, N - 1)
    bc_splits.append(BCSplit(i, total))
bc_splits.sort(reverse=True)
# print(bc_splits)

answer = 0
current_bc_splits_index = 0

for a_last in range(N - 2):
    # a_lastで区切ったときを考える
    sum_A = cum_sum_A.range_sum(0, a_last)
    sum_B_minus = cum_sum_B.range_sum(0, a_last)
    sub_C_minus = cum_sum_C.range_sum(0, a_last)
    while True:
        if bc_splits[current_bc_splits_index].b_last_i <= a_last:
            current_bc_splits_index += 1
        else:
            break
    bc_split = bc_splits[current_bc_splits_index]
    # print(sum_A, bc_split)
    sum_BC = bc_split.total - sum_B_minus
    answer = max(answer, sum_A + sum_BC)

print(answer)
