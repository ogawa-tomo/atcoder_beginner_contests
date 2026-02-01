# WA
class Position:
    def __init__(self):
        self.i = 0
        self.j = 0


T = int(input())
for _ in range(T):
    print("hoge")
    N, C = map(int, input().split())
    grids: list[list[str]] = []
    for _ in range(N):
        s = list(input())
        grids.append(s)
    # print(grids)

    # below_wall[i][j]: (i, j)の下に壁があるか
    below_wall: list[list[bool]] = []
    for i in range(N):
        below_wall.append([False] * N)
    for j in range(N):
        has_wall = False
        for i in range(N - 1, -1, -1):
            if has_wall:
                below_wall[i][j] = True
            else:
                if grids[i][j] == "#":
                    has_wall = True
    # for b in below_wall:
    #     print(b)

    R: list[int] = []
    # i列目について可能か
    for j in range(N):
        p = Position()
        p.i = N - 1
        p.j = C - 1
        while True:
            if p.j > j:
                p.j -= 1
            elif p.j < j:
                p.j += 1
            p.i -= 1

            if below_wall[p.i][p.j]:
                R.append(0)
                break
            if p.i == 0:
                R.append(1)
                break
            if below_wall[p.i - 1][p.j]:
                below_wall[p.i - 1][p.j] = False
    print(R)
