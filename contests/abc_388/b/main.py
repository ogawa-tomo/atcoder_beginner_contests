N, D = map(int, input().split())


class Sneak:
    def __init__(self, T, L):
        self.T = T
        self.L = L


sneaks: list[Sneak] = []
for _ in range(N):
    t, l = map(int, input().split())
    sneaks.append(Sneak(t, l))

for k in range(1, D + 1):
    answer = 0
    for sneak in sneaks:
        heavy = sneak.T * (sneak.L + k)
        answer = max(answer, heavy)
    print(answer)
