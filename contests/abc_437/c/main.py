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


class Tonakai:
    def __init__(self, i: int, weight: int, power: int):
        self.i = i
        self.weight = weight
        self.power = power

    def __lt__(self, other):
        return self.weight < other.weight


T = int(input())
for _ in range(T):
    N = int(input())
    tonakais: list[Tonakai] = []
    for i in range(N):
        w, p = map(int, input().split())
        tonakai = Tonakai(i, w, p)
        tonakais.append(tonakai)
    tonakais.sort()
    weight_list = [tonakai.weight for tonakai in tonakais]
    # print(weight_list)
    cum_sum = CumulativeSum(weight_list)
    weight_cum_sum_list = cum_sum.cumulative_sum_list
    # print(weight_cum_sum_list)

    answer = 0
    for i in range(N):
        # i番目のトナカイは、（自分も乗せるとして）何番目のトナカイまで載せられるか？
        ok = -1
        ng = N
        while ng - ok > 1:
            mid = (ng + ok) // 2
            # if weight_cum_sum_list[mid] <=

    # 自分が含まれていたら引く
