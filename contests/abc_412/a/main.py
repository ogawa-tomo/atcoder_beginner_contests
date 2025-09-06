N = int(input())
answer = 0
for _ in range(N):
    a, b = map(int, input().split())
    if b > a:
        answer += 1

print(answer)
