N = int(input())
A = list(map(int, input().split()))

answer = 0
for i in range(N // 2, N):
    answer += A[i]
print(answer)
