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


N, A, B = map(int, input().split())
S = list(input())

# aだったら1、bだったら0
a_emerge: list[int] = []
b_emerge: list[int] = []
for i in range(N):
    if S[i] == "a":
        a_emerge.append(1)
        b_emerge.append(0)
    else:
        a_emerge.append(0)
        b_emerge.append(1)

# print(a_emerge, b_emerge)

# a, bの累積和
a_cum_sum = CumulativeSum(a_emerge)
b_cum_sum = CumulativeSum(b_emerge)

answer = 0
for left in range(N):
    # aがA個以上となる最小のrightを求める
    if a_cum_sum.range_sum(left, N - 1) < A:
        # そもそも存在しないケース
        continue

    if S[left] == "a" and A == 1:
        ar = left
    else:
        ng = left
        ok = N - 1
        while ok - ng > 1:
            mid = (ng + ok) // 2
            if a_cum_sum.range_sum(left, mid) >= A:
                ok = mid
            else:
                ng = mid
        ar = ok  # aがA個以上となる最小のright

    # bがB個未満となる最大のright
    if b_cum_sum.range_sum(left, N - 1) < B:
        # 全OKのケース
        br = N - 1
    else:
        ok = left
        ng = N - 1
        while ng - ok > 1:
            mid = (ng + ok) // 2
            if b_cum_sum.range_sum(left, mid) < B:
                ok = mid
            else:
                ng = mid
        br = ok  # bがB個未満となる最大のright

    # print(left, ar, br)
    if ar <= br:
        answer += br - ar + 1

print(answer)
