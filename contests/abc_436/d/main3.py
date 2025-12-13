# TLE
from collections import defaultdict
from collections import deque

H, W = map(int, input().split())


class Grid:
    def __init__(self, i: int, j: int, type: str):
        self.i = i
        self.j = j
        self.type = type
        self.neighbors: set[Grid] = set()
        self.distance: int | None = None  # (0, 0)からの距離

    def __repr__(self):
        # return str((self.type, self.neighbors))
        # return self.type
        return str((self.i, self.j, self.type))


# warp_grids["a"]: "a"のグリッドのset
warp_grids: defaultdict[str, set[Grid]] = defaultdict(set)

# warp_grid_repr: "代表点"
# warp_grid_repr: defaultdict[str, Grid] = defaultdict(None)


grids: list[list[Grid]] = []
for i in range(H):
    row = list(input())
    row_data: list[Grid] = []
    for j, r in enumerate(row):
        grid = Grid(i, j, r)
        row_data.append(grid)
        if grid.type != "." and grid.type != "#":
            warp_grids[grid.type].add(grid)

    grids.append(row_data)

# print(grids)
for i in range(H):
    for j in range(W):
        grid = grids[i][j]
        if grid.type != "#":
            # 障害物でないとき、四方のマスを隣に
            vectors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for v in vectors:
                vi = v[0]
                vj = v[1]
                ii = i + vi
                jj = j + vj
                if ii < 0 or ii >= H or jj < 0 or jj >= W:
                    continue
                to_grid = grids[ii][jj]
                if to_grid.type == "#":
                    continue
                grid.neighbors.add(to_grid)
        if grid.type != "#" and grid.type != ".":
            # ワープグリッドだった場合は、全部のワープグリッドを隣に
            grid.neighbors = grid.neighbors | warp_grids[grid.type]
            # for to_grid in warp_grids[grid.type]:
            #     if grid == to_grid:
            #         continue
            #     grid.neighbors.append(to_grid)

# print(warp_grids["b"])
# print(grids[2][0].neighbors)

d: deque[Grid] = deque()

start_grid = grids[0][0]
d.append(start_grid)
start_grid.distance = 0
while d:
    grid = d.popleft()
    if grid.distance is None:
        raise
    distance = grid.distance
    for neighbor in grid.neighbors:
        if neighbor.distance is None:
            d.append(neighbor)
            neighbor.distance = distance + 1

dist = grids[H - 1][W - 1].distance
if dist is None:
    print(-1)
else:
    print(dist)
