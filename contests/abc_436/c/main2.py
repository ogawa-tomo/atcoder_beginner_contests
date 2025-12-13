N, M = map(int, input().split())

grids: set[tuple[int, int]] = set()

answer = 0
for _ in range(M):
    r, c = map(int, input().split())
    r -= 1
    c -= 1

    grid = (r, c)
    exists = False
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            rr = r + dr
            cc = c + dc
            if (rr, cc) in grids:
                exists = True
                break
        if exists:
            break
    if not exists:
        answer += 1
        grids.add(grid)

print(answer)
