# WA
T = int(input())


class Grid:
    def __init__(self, is_black: bool) -> None:
        self.black = is_black
        # self.neighbors: list[Grid] = []
        self.considered = False

    def __repr__(self):
        if self.black:
            return "#"
        else:
            return "."


for _ in range(T):
    H, W = map(int, input().split())
    grids: list[list[Grid]] = []

    def is_block(i: int, j: int):
        return (
            grids[i][j].black
            and grids[i + 1][j].black
            and grids[i][j + 1].black
            and grids[i + 1][j + 1].black
        )

    # def is_wide_block(i: int, j: int):
    #     if j >= W - 2:
    #         return False
    #     return is_block(i, j) and grids[i][j + 2].black and grids[i + 1][j + 2].black

    # def is_long_block(i: int, j: int):
    #     if i >= H - 2:
    #         return False
    #     return is_block(i, j) and grids[i + 2][j].black and grids[i + 2][j + 1].black

    for _ in range(H):
        row: list[Grid] = []
        S = list(input())
        for s in S:
            row.append(Grid(s == "#"))
        grids.append(row)
    # print(grids)
    answer = 0
    for i in range(H - 1):
        for j in range(W - 1):
            grid = grids[i][j]
            if grid.considered:
                continue
            if not is_block(i, j):
                continue
            answer += 1
            # wide_block = is_wide_block(i, j)
            # long_block = is_long_block(i, j)
            # print(i, j, wide_block, long_block)
            max_i = i + 2
            max_j = j + 2
            # if wide_block:
            #     max_j += 1
            # if long_block:
            #     max_i += 1
            for ii in range(i, max_i):
                for jj in range(j, max_j):
                    # print(ii, jj)
                    grids[ii][jj].considered = True

    print(answer)
