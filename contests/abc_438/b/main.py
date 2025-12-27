import sys

N, M = map(int, input().split())

S = list(map(int, list(input())))
T = list(map(int, list(input())))
# print(S, T)

answer = sys.maxsize
for i in range(N - M + 1):
    s = S[i : i + M]
    # print(s)
    tmp = 0
    for j in range(M):
        plus = (s[j] - T[j]) % 10
        # print(plus)
        tmp += plus
    answer = min(answer, tmp)

print(answer)
