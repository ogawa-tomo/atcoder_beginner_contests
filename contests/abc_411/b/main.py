N = int(input())
D = list(map(int, input().split()))

for i in range(N - 1):
    distance = 0
    distances: list[int] = []
    for j in range(i + 1, N):
        distance += D[j - 1]
        distances.append(distance)
    print(" ".join([str(d) for d in distances]))
