from itertools import combinations


class Topping:
    def __init__(self, price: int, value: int) -> None:
        self.price = price
        self.value = value

    def __repr__(self) -> str:
        return str((self.price, self.value))


N, V = map(int, input().split())
W = list(map(int, input().split()))

toppings: list[Topping] = []
for i in range(N):
    w = W[i]
    topping = Topping(i + 1, w)
    toppings.append(topping)

answer = 0
for topping_combination in combinations(toppings, 3):
    # print(topping_combination)
    total_value = 0
    total_price = 0
    for topping in topping_combination:
        total_price += topping.price
        total_value += topping.value
    if total_price <= V:
        answer = max(answer, total_value)

print(answer)
