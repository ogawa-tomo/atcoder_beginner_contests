# やりかけ
from collections import defaultdict


class Grid:
    def __init__(self) -> None:
        self.color = "a"
        self.open = True


class Period:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end


class Change:
    def __init__(self, t: int, color: str) -> None:
        self.t = t
        self.color = color


N, Q = map(int, input().split())

# open_start_by_grid[grid]: グリッドが空いた時刻
open_start_by_grid: defaultdict[Grid, int] = defaultdict(int)

open_periods_by_grid: defaultdict[Grid, list[Period]] = defaultdict(list)

changes: list[Change] = []
grids = [Grid() for _ in range(N)]
for t in range(Q):
    q = list(input())
    if int(q[0]) == 1:
        x = int(q[1])
        x -= 1
        grid = grids[x]
        if grid.open:
            grid.open = False
            period = Period(open_start_by_grid[grid], t)
            open_periods_by_grid[grid].append(period)
        else:
            grid.open = True
            open_start_by_grid[grid] = t
    else:
        c = q[1]
        change = Change(t, c)
        changes.append(change)
