N = int(input())
A = list(map(int, input().split()))

answer = 0
for i in range(N):
    if i % 2 != 0:
        continue
    answer += A[i]
print(answer)
