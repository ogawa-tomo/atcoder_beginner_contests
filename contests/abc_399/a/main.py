N = int(input())
S = list(input())
T = list(input())

answer = 0
for i in range(N):
    if S[i] != T[i]:
        answer += 1

print(answer)
