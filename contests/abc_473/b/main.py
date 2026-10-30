N = int(input())
A = list(map(int, input().split()))

A.sort()
answer = 0
i = 0
while i < N:
    a = A[i]
    if i < N - 1 and a == A[i + 1]:
        i += 2
    else:
        answer += a
        i += 1

print(answer)
