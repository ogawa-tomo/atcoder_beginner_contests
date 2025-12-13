from collections import defaultdict

N, M = map(int, input().split())

# grids: list[list[int]] = []
# for _ in range(N):
#     row = [0] * N
#     grids.append(row)

# grids[r][c]
# grids: defaultdict[defaultdict, [defaultdict, int]] = defaultdict(int)
grids: dict[int, dict[int, int]] = {}
# grids: defaultdict[int, defaultdict[int, int]] = defaultdict(defaultdict(int))
# grids: defaultdict[defaultdict[int, int]] = defaultdict(defaultdict(int))

# print(grids)

answer = 0
for _ in range(M):
    r, c = map(int, input().split())
    r -= 1
    c -= 1

    # if r == 1 and c == 1:
    #     print("debug")
    #     print(r in grids)

    if r in grids:
        if c in grids[r] or (c + 1) in grids[r]:
            continue
    if r + 1 in grids:
        if c in grids[r + 1] or (c + 1) in grids[r + 1]:
            continue

    # if (
    #     r in grids
    #     and (c + 1) in grids[r]
    #     and c in grids[r]
    #     and (r + 1) in grids
    #     and c in grids[r + 1]
    #     and (c + 1) in grids[r + 1]
    # ):
    #     continue
    if not r in grids:
        grids[r] = {}
    grids[r][c] = 1
    grids[r][c + 1] = 1
    if not (r + 1) in grids:
        grids[r + 1] = {}
    grids[r + 1][c] = 1
    grids[r + 1][c + 1] = 1
    # print(r, c)
    # print(grids)

    answer += 1
    # # if grids[r][c] + grids[r + 1][c] + grids[r][c + 1] + grids[r + 1][c + 1] == 0:
    # grids[r][c] = 1
    # grids[r + 1][c] = 1
    # grids[r][c + 1] = 1
    # grids[r + 1][c + 1] = 1
    # answer += 1

print(answer)
