class Grid:
    def __init__(self) -> None:
        self.color = "a"
        self.open = True

    def __repr__(self) -> str:
        return self.color


class Period:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def __repr__(self) -> str:
        return str((self.start, self.end))


class Change:
    def __init__(self, t: int, color: str) -> None:
        self.t = t
        self.color = color

    def __repr__(self) -> str:
        return str((self.t, self.color))


class Tile:
    def __init__(self, grid: Grid) -> None:
        self.grid = grid


N, Q = map(int, input().split())

grids = [Grid() for _ in range(N)]
queries: list[Tile | Change] = []
for t in range(Q):
    q = input().split()
    if int(q[0]) == 1:
        x = int(q[1])
        x -= 1
        grid = grids[x]
        grid.open = not grid.open
        queries.append(Tile(grid))
    else:
        c = q[1]
        change = Change(t, c)
        queries.append(change)

# openな状態で、まだ色が確定していないマス
target_grids: set[Grid] = set()
# closeな状態で、まだ色が確定していないマス
waiting_grids: set[Grid] = set()
for grid in grids:
    if grid.open:
        target_grids.add(grid)
    else:
        waiting_grids.add(grid)
queries.reverse()
for query in queries:
    if isinstance(query, Tile):
        grid = query.grid
        if grid.open and grid in target_grids:
            grid.open = False
            target_grids.remove(grid)
            waiting_grids.add(grid)
        elif (not grid.open) and grid in waiting_grids:
            grid.open = True
            waiting_grids.remove(grid)
            target_grids.add(grid)
    else:
        color = query.color
        for grid in target_grids:
            grid.color = color
        target_grids = set()


print("".join([grid.color for grid in grids]))
