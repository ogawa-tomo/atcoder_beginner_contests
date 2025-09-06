N = int(input())
A = list(map(int, input().split()))
K = int(input())

answer = 0
for a in A:
    if K <= a:
        answer += 1
print(answer)
