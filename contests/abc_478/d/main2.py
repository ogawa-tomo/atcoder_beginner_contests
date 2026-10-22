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

# covers_dict[value]: 値がvalueであるcoverのリスト
covers_dict: dict[int, list[Cover]] = {}
for _ in range(Q):
    l, r, x = map(int, input().split())
    l -= 1
    r -= 1
    cover = Cover(l, r, x)
    if x in covers_dict:
        covers_dict[x].append(cover)
    else:
        covers_dict[x] = [cover]
# print(covers_dict)

# それぞれのvalueについて、重なっているcoverをまとめる
# covers: coverのリスト（同じvalueの区間重複なし）
covers: list[Cover] = []
for value in covers_dict:
    covers_for_value = covers_dict[value]
    covers_for_value.sort(key=lambda c: c.left)
    length = len(covers_for_value)
    i = 0
    while i < length:
        cover = covers_for_value[i]
        while i < length - 1 and cover.right >= covers_for_value[i + 1].left:
            next_cover = covers_for_value[i + 1]
            cover = Cover(cover.left, max(cover.right, next_cover.right), value)
            i += 1
        covers.append(cover)
        i += 1

print(*covered(covers, N))
