# AC
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


T = int(input())
for _ in range(T):
    N, W = map(int, input().split())
    C = list(map(int, input().split()))

    mod = 2 * W

    cum_sum = CumulativeSum(C)

    total = sum(C)

    # costs[m]: m番目のセットのコスト
    costs: list[int] = []
    for m in range(W):
        # m番目のコストを計算する
        m_cost = 0
        start = m
        while True:
            end = start + W - 1
            if start >= N:
                break
            if end >= N:
                m_cost += cum_sum.range_sum(start, N - 1)
                break

            m_cost += cum_sum.range_sum(start, end)
            start += mod
        costs.append(m_cost)
        costs.append(total - m_cost)
    print(min(costs))
