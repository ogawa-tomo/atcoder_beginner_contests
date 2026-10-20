class Okazu:
    def __init__(self, oishisa: int, volume: int) -> None:
        self.oishisa = oishisa
        self.volume = volume


N, W = map(int, input().split())

# print(2**20)

okazu_list: list[Okazu] = []
for _ in range(N):
    a, b = map(int, input().split())
    okazu = Okazu(a, b)
    okazu_list.append(okazu)

answer = 0
for i in range(1 << N):
    total_volume = 0
    total_oishisa = 0
    for j in range(N):
        if i & (1 << j):
            okazu = okazu_list[j]
            total_volume += okazu.volume
            total_oishisa += okazu.oishisa
    if total_volume <= W:
        answer = max(answer, total_oishisa)

print(answer)
