H, W = map(int, input().split())


class Grid:
    def __init__(self, is_black: bool):
        self.is_black = is_black
        self.neighbors: list[Grid] = []

    def __repr__(self):
        if self.is_black:
            return "#"
        else:
            return "."

    def next_black(self):
        if self.is_black:
            return False
        black_count = 0
        for neighbor in self.neighbors:
            if neighbor.is_black:
                black_count += 1
        return black_count == 1


grids: list[list[Grid]] = []
for i in range(H):
    row: list[Grid] = []
    data = list(input())
    for d in data:
        row.append(Grid(d == "#"))
    grids.append(row)

for i in range(H):
    for j in range(W):
        grid = grids[i][j]
        if i > 0:
            grid.neighbors.append(grids[i - 1][j])
        if j > 0:
            grid.neighbors.append(grids[i][j - 1])
        if i < H - 1:
            grid.neighbors.append(grids[i + 1][j])
        if j < W - 1:
            grid.neighbors.append(grids[i][j + 1])

current_blacks: list[Grid] = []
for i in range(H):
    for j in range(W):
        grid = grids[i][j]
        if grid.is_black:
            current_blacks.append(grid)

while current_blacks:
    next_blacks: list[Grid] = []
    for current_black in current_blacks:
        for neighbor in current_black.neighbors:
            if neighbor.next_black():
                next_blacks.append(neighbor)
    for next_black in next_blacks:
        next_black.is_black = True
    current_blacks = next_blacks

answer = 0
for i in range(H):
    for j in range(W):
        grid = grids[i][j]
        if grid.is_black:
            answer += 1
print(answer)
