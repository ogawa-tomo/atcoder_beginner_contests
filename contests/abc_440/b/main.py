N = int(input())
T = list(map(int, input().split()))


class Horse:
    def __init__(self, i: int, t: int):
        self.i = i
        self.t = t

    def __lt__(self, other):
        return self.t < other.t

    def __repr__(self):
        return str(self.i)


horses: list[Horse] = []
for i, t in enumerate(T):
    horse = Horse(i + 1, t)
    horses.append(horse)

horses.sort()
print(*horses[:3])
