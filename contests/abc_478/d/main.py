class Cover:
    def __init__(self, left: int, right: int, value: int):
        self.left = left
        self.right = right
        self.value = value

    def __repr__(self) -> str:
        return str((self.left, self.right, self.value))


# 座標ごとに覆われている数のリストを返す
def covered(covers: list[Cover], length: int):
    # 出席者数の前日比
    x = [0] * (length + 1)
    for cover in covers:
        x[cover.left] += 1
        x[cover.right + 1] -= 1

    # 累積和
    covered_list: list[int] = []
    total = 0
    for i in range(length):
        total += x[i]
        covered_list.append(total)

    return covered_list


N, Q = map(int, input().split())

# covers[value]: 値がvalueであるcoverのリスト
covers: dict[int, list[Cover]] = {}
for _ in range(Q):
    l, r, x = map(int, input().split())
    l -= 1
    r -= 1
    cover = Cover(l, r, x)
    if x in covers:
        covers[x].append(cover)
    else:
        covers[x] = [cover]
# print(covers)

# それぞれのvalueについて、重なっているcoverをまとめる
# new_covers[value]: 値がvalueであるcoverのリスト（ただし重複区間なし）
new_covers: dict[int, list[Cover]] = {}
for value in covers:
    covers[value].sort(key=lambda c: c.left)
    new_covers_list: list[Cover] = []
    length = len(covers[value])
    i = 0
    while i < length:
        cover = covers[value][i]
        while i < length - 1 and cover.right >= covers[value][i + 1].left:
            next_cover = covers[value][i + 1]
            cover = Cover(cover.left, max(cover.right, next_cover.right), value)
            i += 1
        new_covers_list.append(cover)
        i += 1
    new_covers[value] = new_covers_list

# print(new_covers)

# new_covers2: coverのリスト（valueの重複なし）
new_covers2: list[Cover] = []
for value in new_covers:
    new_covers2.extend(new_covers[value])

covered_list = covered(new_covers2, N)
print(*covered_list)
