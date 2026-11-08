N, Q = map(int, input().split())
K = list(map(int, input().split()))

cards = [N - i for i in range(N)]
# print(cards)
for k in K:
    out = cards[N - k :]
    cards = cards[: N - k]
    out.reverse()
    for c in out:
        cards.append(-c)

    # print(cards)
cards.reverse()
for c in cards:
    print(c)
