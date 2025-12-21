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
        self.total = weight + power

    def __lt__(self, other):
        return self.total < other.total


T = int(input())
for _ in range(T):
    N = int(input())
    tonakais: list[Tonakai] = []
    total_power = 0
    total_weight = 0
    for i in range(N):
        w, p = map(int, input().split())
        tonakai = Tonakai(i, w, p)
        tonakais.append(tonakai)
        total_power += p
    tonakais.sort()
    # print(total_power, total_weight)

    # はじめは全員ひく側
    # 合計が小さい方から乗せる
    answer = 0
    for tonakai in tonakais:
        total_power -= tonakai.power
        total_weight += tonakai.weight
        # print(total_weight, total_power)
        if total_weight > total_power:
            break
        answer += 1
    print(answer)
