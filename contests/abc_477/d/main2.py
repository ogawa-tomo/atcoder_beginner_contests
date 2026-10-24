# TLE
from collections import defaultdict


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


N, Q = map(int, input().split())

close_start_by_grid: defaultdict[Grid, int] = defaultdict(int)

close_periods_by_grid: defaultdict[Grid, list[Period]] = defaultdict(list)

changes: list[Change] = []
grids = [Grid() for _ in range(N)]
for t in range(Q):
    q = input().split()
    if int(q[0]) == 1:
        x = int(q[1])
        x -= 1
        grid = grids[x]
        if grid.open:
            grid.open = False
            close_start_by_grid[grid] = t
            # period = Period(open_start_by_grid[grid], t)
            # open_periods_by_grid[grid].append(period)
        else:
            grid.open = True
            period = Period(close_start_by_grid[grid], t)
            close_periods_by_grid[grid].append(period)
            # open_start_by_grid[grid] = t
    else:
        c = q[1]
        change = Change(t, c)
        changes.append(change)

for grid in grids:
    if not grid.open:
        period = Period(close_start_by_grid[grid], Q - 1)
        close_periods_by_grid[grid].append(period)
# print(close_periods_by_grid)


def is_open(t: int, grid: Grid):
    close_periods = close_periods_by_grid[grid]
    if not close_periods:
        return True
    ok = -1
    ng = len(close_periods)
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if close_periods[mid].start <= t:
            ok = mid
        else:
            ng = mid

    if ok == -1:
        return True
    period = close_periods[ok]
    return t > period.end


remaining_grids = set(grids)
changes.reverse()
for change in changes:
    remove_grids: list[Grid] = []
    for grid in remaining_grids:
        if is_open(change.t, grid):
            grid.color = change.color
            # remaining_grids.remove(grid)
            remove_grids.append(grid)
    for grid in remove_grids:
        remaining_grids.remove(grid)

print("".join([grid.color for grid in grids]))
