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


# original_aliens: list[Alien] = []
aliens: list[Alien] = []
for a in A:
    aliens.append(Alien(a))
    # original_aliens.append(Alien(a))

for i, alien in enumerate(aliens):
    give_stone_num = min(N - i - 1, alien.stone_num)
    alien.stone_num -= give_stone_num
    for index in range(1, give_stone_num + 1):
        given_alien = aliens[i + index]
        given_alien.stone_num += 1

print(" ".join([str(alien.stone_num) for alien in aliens]))
