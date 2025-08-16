N, M = map(int, input().split())

S = list(input())
T = list(input())

# select[i]: 累積和の値が偶数ならS、奇数ならT
select = [0] * N

for _ in range(M):
    L, R = map(int, input().split())
    L -= 1
    R -= 1
    select[L] += 1
    if R < N - 1:
        select[R + 1] -= 1

answer: list[str] = []
agg = 0
for i in range(N):
    agg += select[i]
    if agg % 2 == 0:
        answer.append(S[i])
    else:
        answer.append(T[i])

print("".join([a for a in answer]))
