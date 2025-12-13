N = int(input())

grids: list[list[int]] = []
for _ in range(N):
    row = [-1] * N
    grids.append(row)

# print(grids)

# current = (0, (N - 1) // 2)
r = 0
c = (N - 1) // 2
k = 1
grids[0][(N - 1) // 2] = k
for _ in range(N**2 - 1):
    r1 = (r - 1) % N
    c1 = (c + 1) % N
    if grids[r1][c1] == -1:
        r = r1
        c = c1
    else:
        r = (r + 1) % N

    k += 1
    grids[r][c] = k

# print(grids)
for row in grids:
    print(*row)
