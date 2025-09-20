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

    def right_grid(i: int, j: int):
        if j == W - 1:
            return Grid(False)
        return grids[i][j + 1]

    def left_grid(i: int, j: int):
        if j == 0:
            return Grid(False)
        return grids[i][j - 1]

    def upper_grid(i: int, j: int):
        if i == 0:
            return Grid(False)
        return grids[i - 1][j]

    def below_grid(i: int, j: int):
        if i == H - 1:
            return Grid(False)
        return grids[i + 1][j]

    def upper_left_grid(i: int, j: int):
        if i == 0 or j == 0:
            return Grid(False)
        return grids[i - 1][j - 1]

    def upper_right_grid(i: int, j: int):
        if i == 0 or j == W - 1:
            return Grid(False)
        return grids[i - 1][j + 1]

    def below_left_grid(i: int, j: int):
        if i == H - 1 or j == 0:
            return Grid(False)
        return grids[i + 1][j - 1]

    def below_right_grid(i: int, j: int):
        if i == H - 1 or j == W - 1:
            return Grid(False)
        return grids[i + 1][j + 1]

    def is_upper_left_blocK(i: int, j: int):
        return (
            (left_grid(i, j).black and not left_grid(i, j).considered)
            and (upper_grid(i, j).black and not upper_grid(i, j).considered)
            and (upper_left_grid(i, j).black and not upper_left_grid(i, j).considered)
        )

    def is_upper_right_block(i: int, j: int):
        return (
            (right_grid(i, j).black and not right_grid(i, j).considered)
            and (upper_grid(i, j).black and not upper_grid(i, j).considered)
            and (upper_right_grid(i, j).black and not upper_right_grid(i, j).considered)
        )

    def is_below_left_block(i: int, j: int):
        return (
            (left_grid(i, j).black and not left_grid(i, j).considered)
            and (below_grid(i, j).black and not below_grid(i, j).considered)
            and (below_left_grid(i, j).black and not below_left_grid(i, j).considered)
        )

    def is_below_right_block(i: int, j: int):
        return (
            (right_grid(i, j).black and not right_grid(i, j).considered)
            and (below_grid(i, j).black and not below_grid(i, j).considered)
            and (below_right_grid(i, j).black and not below_right_grid(i, j).considered)
        )

    for _ in range(H):
        row: list[Grid] = []
        S = list(input())
        for s in S:
            row.append(Grid(s == "#"))
        grids.append(row)
    # print(grids)
    answer = 0
    for i in range(H):
        for j in range(W):
            grid = grids[i][j]
            if grid.considered or not grid.black:
                continue
            grid.considered = True
            block = False
            if is_below_left_block(i, j):
                block = True
                grid.considered = True
                for ii in range(i, i + 2):
                    for jj in range(j - 1, j + 1):
                        grids[ii][jj].considered = True
            if is_below_right_block(i, j):
                block = True
                grid.considered = True
                for ii in range(i, i + 2):
                    for jj in range(j, j + 2):
                        grids[ii][jj].considered = True
            if is_upper_left_blocK(i, j):
                block = True
                grid.considered = True
                for ii in range(i - 1, i + 1):
                    for jj in range(j - 1, j + 1):
                        grids[ii][jj].considered = True
            if is_upper_right_block(i, j):
                block = True
                grid.considered = True
                for ii in range(i - 1, i + 1):
                    for jj in range(j, j + 2):
                        grids[ii][jj].considered = True
            if block:
                answer += 1

    print(answer)
