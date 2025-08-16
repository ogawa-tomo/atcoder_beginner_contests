Q = int(input())
fukuro: list[int] = []
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        fukuro.append(query[1])
        fukuro.sort()
    if query[0] == 2:
        print(fukuro.pop(0))
