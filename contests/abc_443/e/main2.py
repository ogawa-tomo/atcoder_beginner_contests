# AC
from collections import defaultdict


class Grid:
    def __init__(self, i: int, j: int, is_empty: bool):
        self.i = i
        self.j = j
        self.is_empty = is_empty
        self.reacheble = False

    @property
    def answer(self):
        if self.reacheble:
            return str(1)
        else:
            return str(0)

    def __repr__(self) -> str:
        return str((self.i, self.j))


T = int(input())
for _ in range(T):
    N, C = map(int, input().split())
    grids: list[list[Grid]] = []
    for i in range(N):
        data = list(input())
        row: list[Grid] = []
        for j, d in enumerate(data):
            grid = Grid(i, j, d != "#")
            row.append(grid)
        grids.append(row)
    # print(grids)

    # lowest_wall[j]: j列目の一番下の壁
    lowest_wall: dict[int, Grid | None] = dict()
    for j in range(N):
        for i in range(N - 1, -1, -1):
            grid = grids[i][j]
            if not grid.is_empty:
                lowest_wall[j] = grid
                break
        else:
            lowest_wall[j] = None

    # ok_column[j]: j列目がOKかどうか
    ok_column = defaultdict(bool)

    # dp
    grids[N - 1][C - 1].reacheble = True
    ok_column[C - 1] = True
    for i in range(N - 1, 0, -1):
        for j in range(N):
            grid = grids[i][j]
            if not grid.reacheble:
                continue
            for jj in [j - 1, j, j + 1]:
                if jj < 0 or N <= jj:
                    continue
                target_grid = grids[i - 1][jj]
                if target_grid.reacheble:
                    continue
                if target_grid.is_empty:
                    target_grid.reacheble = True
                else:
                    if ok_column[jj] or target_grid == lowest_wall[jj]:
                        target_grid.reacheble = True
                        ok_column[jj] = True

    print("".join([g.answer for g in grids[0]]))
