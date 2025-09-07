N = int(input())
S: list[str] = []

length = 0
for _ in range(N):
    query = list(input().split())
    c = query[0]
    l = int(query[1])
    length += l
    if length > 100:
        print("Too Long")
        exit()
    S.extend([c] * l)

print("".join(S))
