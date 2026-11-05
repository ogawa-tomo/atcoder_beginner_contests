# AC
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A2 = A.copy()

# A[0] % 2 == 0のとき
answer1 = 0
if A[0] % 2 == 1:
    A[0] += 1
    answer1 += 1
for i in range(1, N):
    if (A[i - 1] + A[i]) % 2 != B[i - 1]:
        A[i] += 1
        answer1 += 1

# A[0] % 2 == 1のとき
answer2 = 0
if A2[0] % 2 == 0:
    A2[0] += 1
    answer2 += 1
for i in range(1, N):
    if (A2[i - 1] + A2[i]) % 2 != B[i - 1]:
        A2[i] += 1
        answer2 += 1

print(min(answer1, answer2))
