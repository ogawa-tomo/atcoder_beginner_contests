X, Y, L, R, A, B = map(int, input().split())

answer = 0
for t in range(A, B):
    if L <= t < R:
        answer += X
    else:
        answer += Y

print(answer)
