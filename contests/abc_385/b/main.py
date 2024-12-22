H, W, X, Y = map(int, input().split())
X -= 1
Y -= 1
grids: list[list[str]] = []
# grids = []
for _ in range(H):
    row = list(input())
    grids.append(row)
# print(grids)
T = list(input())
# print(T)


def tooreru(grid: str) -> bool:
    return grid == "." or grid == "@"


# class House:
#     def __init__(self, i, j):
#         self.i = i
#         self.j = j
#         self.visited = False

# houses[i-j]: i,jにある家を訪れたか
houses = {}
for i in range(H):
    for j in range(W):
        if grids[i][j] == "@":
            houses[f"{i}-{j}"] = False


for t in T:
    if t == "U" and X - 1 >= 0 and tooreru(grids[X - 1][Y]):
        X -= 1
    elif t == "D" and X + 1 < H and tooreru(grids[X + 1][Y]):
        X += 1
    elif t == "L" and Y - 1 >= 0 and tooreru(grids[X][Y - 1]):
        Y -= 1
    elif t == "R" and Y + 1 < W and tooreru(grids[X][Y + 1]):
        Y += 1
    if grids[X][Y] == "@":
        houses[f"{X}-{Y}"] = True

visited = 0
for v in houses.values():
    if v:
        visited += 1

print(X + 1, Y + 1, visited)
