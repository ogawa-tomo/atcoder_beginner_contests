N = int(input())
A = list(map(int, input().split()))


class Alien:
    def __init__(self, stone_num):
        self.stone_num = stone_num
        self.is_adult = False

    def __repr__(self):
        return str(self.stone_num)

    def __lt__(self, other):
        return self.stone_num < other.stone_num


aliens: list[Alien] = []
for a in A:
    aliens.append(Alien(a))

# morau[i]: i番目のエイリアンがもらう石の数
morau = [0] * N
# morau_sa[i]: i番目のエイリアンがもらう石の数と、i-1番目のエイリアンがもらう石の数の差
morau_sa = [0] * N

for i, alien in enumerate(aliens):
    # 石をもらう
    if i > 0:
        morau[i] = morau[i - 1] + morau_sa[i]
    alien.stone_num += morau[i]

    # 石をあげる
    give_stone_num = min(N - i - 1, alien.stone_num)
    alien.stone_num -= give_stone_num
    if give_stone_num > 0:
        morau_sa[i + 1] += 1
        if i + give_stone_num + 1 < N:
            morau_sa[i + give_stone_num + 1] -= 1

print(" ".join([str(alien.stone_num) for alien in aliens]))
