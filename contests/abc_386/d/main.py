N, M = map(int, input().split())

# 塗られていないマスは"N"
# grids = []
# for _ in range(N):
#     grids.append(["N" for _ in range(N)])
# print(grids)

# row_black[x]: 上からx行目の、Bの境目（row_black[2] = 3であれば、2行目は3列目より左はB
# row_white[x]: 上からx行目の、Wの境目（row_white[2] = 5であれば、2行目は5列目より右はW
# row_black: dict[int, int] = {}
# row_white: dict[int, int] = {}

# column_black[y]: 左からy列目の、Bの境目（column_black[3] = 5であれば、3列目は5行目より上はB
# column_white[y]: 左からy列目の、Wの境目（column_black[3] = 7であれば、3列目は7行目より下はB
# column_black: dict[int, int] = {}
# column_white: dict[int, int] = {}


class Grid:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# 右下にあるB
migisita_b: list[Grid] = []

hidariue_w: list[Grid] = []

for _ in range(M):
    x_input, y_input, c = input().split()
    x = int(x_input) - 1
    y = int(y_input) - 1
    # print(x, y, c)
    if c == "B":
        migisita_b.append(Grid(x, y))
        for w in hidariue_w:
            if w.x <= x and w.y <= y:
                print("No")
                exit()
    if c == "W":
        hidariue_w.append(Grid(x, y))
        for b in migisita_b:
            if b.x >= x and b.y >= y:
                print("No")
                exit()

print("Yes")
