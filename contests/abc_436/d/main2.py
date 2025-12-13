# だめ
from collections import defaultdict
from collections import deque

H, W = map(int, input().split())


class Grid:
    def __init__(self, i: int, j: int, type: str):
        self.i = i
        self.j = j
        self.type = type
        self.neighbors: list[Grid] = []
        self.distance: int | None = None  # (0, 0)からの距離

    def __repr__(self):
        # return str((self.type, self.neighbors))
        # return self.type
        return str((self.i, self.j, self.type))


# # warp_grids["a"]: "a"のグリッド（代表）
warp_grids: defaultdict[str, Grid] = defaultdict(None)

# O(10^6)
grids: list[list[Grid]] = []
for i in range(H):
    row = list(input())
    row_data: list[Grid] = []
    for j, r in enumerate(row):
        grid = Grid(i, j, r)
        row_data.append(grid)
        if grid.type != "." and grid.type != "#":
            # 代表点をとる
            warp_grids[grid.type] = grid
    grids.append(row_data)

# print(warp_grids)
# for key in warp_grids:
#     print(key)

# # print(grids)
for i in range(H):
    for j in range(W):
        grid = grids[i][j]
        if grid.type != "#":
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

                if grid.type == ".":
                    # 自分が普通のグリッドだったら
                    if to_grid.type == ".":
                        # 隣が普通のグリッドだったら
                        grid.neighbors.append(to_grid)
                    else:
                        # 隣がワープグリッドだったら、ワープグリッドの代表点を加える
                        grid.neighbors.append(warp_grids[to_grid.type])
                else:
                    # 自分がワープグリッドだったら
                    repr_grid = warp_grids[grid.type]  # 代表点をとる
                    if to_grid.type == ".":
                        repr_grid.neighbors.append(to_grid)
                    else:
                        # 隣もワープグリッドだったら、代表点を加える
                        to_repr_grid = warp_grids[to_grid.type]  # 隣の代表点
                        if repr_grid != to_repr_grid:
                            repr_grid.neighbors.append(to_repr_grid)
        # if grid.type != "#" and grid.type != ".":
        #     for to_grid in warp_grids[grid.type]:
        #         if grid == to_grid:
        #             continue
        #         grid.neighbors.append(to_grid)

# # print(warp_grids["b"])
# # print(grids[2][0].neighbors)


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
