N, K = map(int, input().split())
A = list(map(int, input().split()))

answer = 0
for i in range(N - 1):
    y = A[i]
    next_y = A[i + 1]

    if i == 0 and y == K:
        answer += 1

    if (y < K and K <= next_y) or (K < y and next_y <= K):
        answer += 1

print(answer)
