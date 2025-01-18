Q = int(input())


class Sneak:
    def __init__(self, length: int, x: int):
        self.length = length
        self.x = x

    def __repr__(self):
        return str(self.x)


sneaks: list[Sneak] = []
current_head_sneak_index = 0
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        length = query[1]
        if len(sneaks) == 0:
            sneak = Sneak(length, 0)
            sneaks.append(sneak)
        else:
            last_sneak = sneaks[-1]
            sneak = Sneak(length, last_sneak.x + last_sneak.length)
            sneaks.append(sneak)
    if query[0] == 2:
        current_head_sneak_index += 1

    if query[0] == 3:
        k = query[1]
        head_sneak = sneaks[current_head_sneak_index]
        sneak = sneaks[current_head_sneak_index + k - 1]
        # print(sneaks)
        print(sneak.x - head_sneak.x)
