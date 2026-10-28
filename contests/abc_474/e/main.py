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

    goods.sort(key=lambda g: g.a)
    coupon_price = min(goods, key=lambda g: g.a).a
    # print(coupon_price)
    # coupon_price = goods[0].a  # 最も安く手に入るクーポン
    # print(coupon_price)
    #

    should_use_coupon_goods = 0
    for good in goods:
        if good.ab_diff > coupon_price:
            # クーポンを買ったほうがいい商品
            good.should_use_coupon = True
            should_use_coupon_goods += 1

    answer = 0
    current_coupons = 0
    goods.sort(key=lambda g: g.ab_diff)
    for good in goods:
        # print(good)
        if not good.should_use_coupon:
            # クーポンの枚数が足りてないのなら、ゲットしておく
            if current_coupons < should_use_coupon_goods:
                # print("クーポンゲット")
                answer += good.a
                current_coupons += 1
                good.bought = True
            else:
                # print("まだ買わない")
                pass
                # answer += good.b
        else:
            answer += good.b
            # クーポンがあれば、それを使う
            if current_coupons > 0:
                # print("クーポン使って買う")
                current_coupons -= 1
                good.bought = True
            else:
                # クーポンがなければ、作る
                # print("クーポン作って買う")
                answer += coupon_price
                good.bought = True

    remaining_goods: list[Good] = []
    for good in goods:
        if not good.bought:
            remaining_goods.append(good)

    length = len(remaining_goods)
    coupon_i = length // 2
    current_coupons = 0
    for i in range(length):
        good = remaining_goods[i]
        if i < coupon_i:
            answer += good.a
            current_coupons += 1
        else:
            if i == coupon_i and length % 2 == 1:
                answer += good.a
            else:
                answer += good.b

    # for good in goods:
    #     if good.bought:
    #         continue
    #     print(good)
    #     if current_coupons > 0:
    #         print("余ったクーポンで買う")
    #         answer += good.b
    #         current_coupons -= 1
    #     else:
    #         print("クーポンが余ってないので定額で買う")
    #         answer += good.a

    print(answer)
