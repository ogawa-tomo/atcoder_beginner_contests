# AC
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


class Good:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b
        self.ab_diff = a - b
        self.should_use_coupon = False
        self.bought = False

    def __repr__(self) -> str:
        return str((self.a, self.b))


T = int(input())

for _ in range(T):
    N = int(input())

    goods: list[Good] = []
    for _ in range(N):
        a, b = map(int, input().split())
        good = Good(a, b)
        goods.append(good)

    goods.sort(key=lambda g: g.ab_diff, reverse=True)
    min_coupon_good = min(goods, key=lambda g: g.a)

    a_list: list[int] = []
    b_list: list[int] = []
    for good in goods:
        a_list.append(good.a)
        b_list.append(good.b)

    cum_sum_a = CumulativeSum(a_list)
    cum_sum_b = CumulativeSum(b_list)

    # すべての商品をクーポン使わずに買う
    answer = cum_sum_a.range_sum(0, N - 1)

    # iまでの商品をクーポンで買う
    for i in range(N - 1):
        # クーポンで買う商品
        price = cum_sum_b.range_sum(0, i)
        if i < N - 1:
            # クーポンを使わずに買う商品
            price += cum_sum_a.range_sum(i + 1, N - 1)

        # 得られるクーポン
        got_coupon_num = N - 1 - i
        # 必要なクーポン
        needed_coupon_num = i + 1
        # 不足するクーポン
        short_coupon_num = needed_coupon_num - got_coupon_num

        if short_coupon_num > 0:
            price += min_coupon_good.a * short_coupon_num

        answer = min(answer, price)

    print(answer)
