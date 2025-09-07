N, L, R = map(int, input().split())
answer = 0
for _ in range(N):
    x, y = map(int, input().split())
    if x <= L and R <= y:
        answer += 1

print(answer)
