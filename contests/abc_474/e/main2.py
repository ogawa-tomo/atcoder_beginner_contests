# WA
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

    goods.sort(key=lambda g: g.ab_diff)

    answer = 0
    for i in range(N):
        another_i = N - i - 1
        if i >= another_i:
            break
        good = goods[i]
        another_good = goods[another_i]

        if another_good.ab_diff >= good.ab_diff:
            answer += good.a
            good.bought = True
            answer += another_good.b
            another_good.bought = True

    min_coupon_good = min(goods, key=lambda g: g.a)

    # 残ったものは全部ab_diffが一緒
    remaining_goods: list[Good] = []
    for good in goods:
        if not good.bought:
            remaining_goods.append(good)

    length = len(remaining_goods)
    i = 0
    while i < length:
        good = remaining_goods[i]
        if i < length - 1:
            next_good = remaining_goods[i + 1]
            # if good.a + next_good.b < 2*(good.b + min_coupon_good.c):
            answer += min(good.a + next_good.b, 2 * (good.b + min_coupon_good.b))
            i += 2
        else:
            if good.ab_diff > min_coupon_good.a:
                answer += good.b + min_coupon_good.a
            else:
                answer += good.a
            i += 1

    # for good in goods:
    #     if good.bought:
    #         continue
    #     if good == min_coupon_good:
    #         continue
    #     if good.ab_diff > min_coupon_good.a:
    #         answer += good.b
    #         good.bought = True
    #         answer += min_coupon_good.a
    #         min_coupon_good.bought = True
    #
    # if not min_coupon_good.bought:
    #     answer += min_coupon_good.b
    #     min_coupon_good.bought = True

    print(answer)
