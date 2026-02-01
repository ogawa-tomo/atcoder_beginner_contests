import math

N, M = map(int, input().split())


class Researcher:
    def __init__(self, i: int):
        self.i = i
        self.to_reseacher: list[Researcher] = []

    @property
    def sadoku_num(self):
        return N - 1 - len(self.to_reseacher)

    def __repr__(self):
        return str(self.sadoku_num)


researchers = [Researcher(i) for i in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    ra = researchers[a]
    rb = researchers[b]
    ra.to_reseacher.append(rb)
    rb.to_reseacher.append(ra)

answers: list[int] = []
for r in researchers:
    # print(r.sadoku_num)
    answers.append(math.comb(r.sadoku_num, 3))

# print(researchers)
# print(math.comb(3, 3))
print(*answers)
