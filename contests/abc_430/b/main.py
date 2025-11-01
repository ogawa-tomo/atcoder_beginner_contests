N, M = map(int, input().split())

grids: list[list[str]] = []
for _ in range(N):
    grids.append(list(input()))

# print(grids)
# patterns: set[list[list[str]]] = set()
patterns: set[str] = set()
for i in range(N - M + 1):
    for j in range(N - M + 1):
        # pattern: list[list[str]] = []
        pattern = ""
        for ii in range(M):
            row: list[str] = []
            for jj in range(M):
                # row.append(grids[i + ii][j + jj])
                pattern += grids[i + ii][j + jj]
            # pattern.append(row)
        # print(pattern)
        patterns.add(pattern)

print(len(patterns))
