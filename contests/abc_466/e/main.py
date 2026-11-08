class Card:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b
        self.is_front = True

    def reverse(self):
        self.is_front = not self.is_front

    @property
    def value(self):
        if self.is_front:
            return self.a
        else:
            return self.b

    @property
    def reverse_profit(self):
        if self.is_front:
            return self.b - self.a
        else:
            return self.a - self.b


N, K = map(int, input().split())

cards: list[Card] = []
for _ in range(N):
    a, b = map(int, input().split())
    card = Card(a, b)
    cards.append(card)

for _ in range(K):
    max_profit_left = 0
    max_profit_right = 0
    max_profit = 0
    profit = 0

    right = 0
    for left in range(N):
        left_card = cards[left]
        if right <= left:
            right = left
            profit = left_card.reverse_profit
        if left_card.reverse_profit <= 0:
            profit -= left_card.reverse_profit
            continue

        if profit > max_profit:
            max_profit = profit
            max_profit_left = left
            max_profit_right = right
        while right + 1 < N and profit + cards[right + 1].reverse_profit > 0:
            right += 1
            profit += cards[right].reverse_profit
            if profit > max_profit:
                max_profit = profit
                max_profit_left = left
                max_profit_right = right

        profit -= left_card.reverse_profit

    if max_profit > 0:
        for i in range(max_profit_left, max_profit_right + 1):
            cards[i].reverse()
    else:
        break

answer = 0
for card in cards:
    answer += card.value
print(answer)
