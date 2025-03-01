N = int(input())

grids: list[list[str]] = []

for i in range(N):
    row: list[str] = []
    for j in range(N):
        row.append("none")
    grids.append(row)

# print(grids)

for i in range(N):
    j = N - 1 - i
    if i % 2 == 0:
        color = "#"
    else:
        color = "."
    if i <= j:
        for x in range(i, j + 1):
            for y in range(i, j + 1):
                grids[x][y] = color

for i in range(N):
    print("".join(grids[i]))
