from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))

# d[k][i]: k桁の数を足したとき、余りがiになる数の数
d: list[defaultdict[int, int]] = []
for _ in range(12):
    d.append(defaultdict(int))

for a in A:
    for k in range(1, 12):
        value = a * 10**k
        r = value % M
        d[k][r] += 1

answer = 0
for a in A:
    k = len(str(a))
    r = a % M
    if r == 0:
        answer += d[k][0]
    else:
        answer += d[k][M - r]

print(answer)
