H, W = map(int, input().split())

grids: list[list[str]] = []

for _ in range(H):
    row = list(input())
    grids.append(row)

# print(grids)

for i in range(H):
    for j in range(W):
        if grids[i][j] == ".":
            continue
        black_num = 0
        # 上
        if i > 0:
            above = grids[i - 1][j]
            if above == "#":
                black_num += 1
        # 下
        if i < H - 1:
            below = grids[i + 1][j]
            if below == "#":
                black_num += 1
        # 左
        if j > 0:
            left = grids[i][j - 1]
            if left == "#":
                black_num += 1
        # 右
        if j < W - 1:
            right = grids[i][j + 1]
            if right == "#":
                black_num += 1

        if black_num != 2 and black_num != 4:
            print("No")
            exit()

print("Yes")
