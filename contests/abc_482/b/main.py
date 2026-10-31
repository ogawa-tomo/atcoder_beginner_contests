grids: list[list[str]] = []
for _ in range(5):
    row = list(input())
    grids.append(row)

# print(grids)

answer = 5

# 行
for i in range(5):
    row = grids[i]
    count = 0
    for j in range(5):
        grid = row[j]
        if grid == "o":
            count += 1

    needed = 5 - count
    answer = min(answer, needed)
# 列
for j in range(5):
    count = 0
    for i in range(5):
        grid = grids[i][j]
        if grid == "o":
            count += 1
    needed = 5 - count
    answer = min(answer, needed)

# 斜め1
count = 0
for i in range(5):
    grid = grids[i][i]
    if grid == "o":
        count += 1
    needed = 5 - count
    answer = min(answer, needed)

# 斜め2
count = 0
for i in range(5):
    grid = grids[i][4 - i]
    if grid == "o":
        count += 1
    needed = 5 - count
    answer = min(answer, needed)
print(answer)
