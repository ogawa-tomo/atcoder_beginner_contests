from collections import deque
import sys

H, W = map(int, input().split())

max_distance = sys.maxsize


class Grid:
    def __init__(self, type: str, i: int, j: int):
        self.type = type
        self.i = i
        self.j = j
        self.neighbors: list[Grid] = []
        self.normal_distance = max_distance
        self.switched_distance = max_distance

    def is_start(self):
        return self.type == "S"

    def is_goal(self):
        return self.type == "G"

    def is_open(self, switched: bool):
        if self.type == "#":
            return False
        if self.type == "o":
            return not switched
        if self.type == "x":
            return switched
        return True

    def is_switch(self):
        return self.type == "?"

    def __repr__(self):
        return self.type


grids: list[list[Grid]] = []
start_i = 0
start_j = 0
goal_i = 0
goal_j = 0
for i in range(H):
    row: list[Grid] = []
    inp = list(input())
    for j, t in enumerate(inp):
        grid = Grid(t, i, j)
        row.append(grid)
        if grid.is_start():
            start_i = i
            start_j = j
        if grid.is_goal():
            goal_i = i
            goal_j = j

    grids.append(row)


# make neighbors
def neighbors(grid: Grid, switched: bool):
    result: list[Grid] = []
    if grid.i > 0:
        g = grids[grid.i - 1][grid.j]
        if g.is_open(switched):
            result.append(g)
    if grid.j > 0:
        g = grids[grid.i][grid.j - 1]
        if g.is_open(switched):
            result.append(g)
    if grid.i < H - 1:
        g = grids[grid.i + 1][grid.j]
        if g.is_open(switched):
            result.append(g)
    if grid.j < W - 1:
        g = grids[grid.i][grid.j + 1]
        if g.is_open(switched):
            result.append(g)
    return result


start_grid = grids[start_i][start_j]
# print(goal_i, goal_j)


class QueueObject:
    def __init__(self, grid: Grid, switched: bool):
        self.grid = grid
        self.switched = switched


d: deque[QueueObject] = deque()
d.append(QueueObject(start_grid, False))
start_grid.normal_distance = 0
while d:
    q = d.popleft()
    switched = q.switched
    grid = q.grid
    if switched:
        distance = grid.switched_distance
    else:
        distance = grid.normal_distance
    if grid.is_switch():
        switched = not switched

    for neighbor in neighbors(grid, switched):
        if switched:
            if neighbor.switched_distance == max_distance:
                d.append(QueueObject(neighbor, switched))
                neighbor.switched_distance = distance + 1
        else:
            if neighbor.normal_distance == max_distance:
                d.append(QueueObject(neighbor, switched))
                neighbor.normal_distance = distance + 1

goal_grid = grids[goal_i][goal_j]
if (
    goal_grid.normal_distance == max_distance
    and goal_grid.switched_distance == max_distance
):
    print(-1)
else:
    print(min(goal_grid.normal_distance, goal_grid.switched_distance))
