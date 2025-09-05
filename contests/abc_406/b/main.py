N, K = map(int, input().split())
A = list(map(int, input().split()))
answer = 1

for a in A:
    answer *= a
    if answer >= 10**K:
        answer = 1

print(answer)
