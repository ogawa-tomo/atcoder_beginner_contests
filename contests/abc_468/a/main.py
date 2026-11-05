N = int(input())
A = list(map(int, input().split()))

answer = 0
for i in range(1, N - 1):
    if A[i - 1] < A[i] and A[i] > A[i + 1]:
        answer += 1

print(answer)
