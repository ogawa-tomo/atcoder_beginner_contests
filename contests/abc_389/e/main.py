import heapq

N, M = map(int, input().split())
P = list(map(int, input().split()))


class Good:
    def __init__(self, price: int):
        self.original_price = price
        self.price = price
        self.k = 1

    def __lt__(self, other):
        return self.price < other.price

    def __repr__(self):
        return str(self.price)


goods: list[Good] = []
for p in P:
    good = Good(p)
    heapq.heappush(goods, good)
print(goods)

kingaku = 0
answer = 0
while True:
    print(goods)
    good = heapq.heappop(goods)
    print(good)
    # print(goods)
    # print(good)
    kingaku += good.price
    print(kingaku)
    if kingaku > M:
        print(answer)
        exit()
    answer += 1
    good.k += 1
    good.price = (good.k**2) * good.original_price - good.price
    heapq.heappush(goods, good)

# 間違ってる
