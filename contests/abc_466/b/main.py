N, M = map(int, input().split())

answer: dict[int, int] = dict()
for k in range(1, M + 1):
    answer[k] = -1
for _ in range(N):
    c, s = map(int, input().split())
    answer[c] = max(answer[c], s)


print(*answer.values())
