H, W = map(int, input().split())
G: list[list[str]] = []
for _ in range(H):
    row = list(input())
    G.append(row)
print(G)
