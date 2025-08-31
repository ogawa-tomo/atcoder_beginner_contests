N = int(input())
A = list(map(int, input().split()))

answer = 0
for i, a in enumerate(A):
    if i % 2 == 0:
        answer += a

print(answer)
