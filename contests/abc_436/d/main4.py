# TLE
from collections import defaultdict
from collections import deque

H, W = map(int, input().split())


class Grid:
    def __init__(self, i: int, j: int, type: str):
        self.i = i
        self.j = j
        self.type = type
        self.neighbors: list[Grid] = []
        self.warp_neighbors: list[Grid] = []
        self.distance: int | None = None  # (0, 0)からの距離

    @property
    def is_warp(self):
        return self.type != "." and self.type != "#"

    def __repr__(self):
        # return str((self.type, self.neighbors))
        # return self.type
        return str((self.i, self.j, self.type))


# warp_grids["a"]: "a"のグリッドのリスト
warp_grids: defaultdict[str, list[Grid]] = defaultdict(list)

# visited_warp["a"]: "a"のワープマスを既に訪れたか
visited_warp: defaultdict[str, bool] = defaultdict(bool)

grids: list[list[Grid]] = []
for i in range(H):
    row = list(input())
    row_data: list[Grid] = []
    for j, r in enumerate(row):
        grid = Grid(i, j, r)
        row_data.append(grid)
        if grid.is_warp:
            warp_grids[grid.type].append(grid)
    grids.append(row_data)

# print(grids)
for i in range(H):
    for j in range(W):
        grid = grids[i][j]
        if grid.type == "#":
            continue
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
            grid.neighbors.append(to_grid)
        if grid.is_warp:
            # 自分自身も追加されるがとくに問題ない
            grid.warp_neighbors = warp_grids[grid.type]


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
    if grid.is_warp and not visited_warp[grid.type]:
        # 既に訪れたことのあるワープマスであれば、ここからのワープを考える必要はない
        visited_warp[grid.type] = True
        for neighbor in grid.warp_neighbors:
            if neighbor.distance is None:
                d.append(neighbor)
                neighbor.distance = distance + 1

dist = grids[H - 1][W - 1].distance
if dist is None:
    print(-1)
else:
    print(dist)
