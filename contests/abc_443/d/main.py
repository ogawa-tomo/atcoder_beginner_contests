import sys

T = int(input())
for _ in range(T):
    N = int(input())
    R = list(map(int, input().split()))

    # min_r[i]: i番目の最小値
    min_r = [10**6] * N

    # 左からmin_rを求める
    for i in range(N):
        r = R[i]
        if i == 0:
            min_r[i] = r
            continue
        if r >= min_r[i - 1] + 1:
            min_r[i] = min_r[i - 1] + 1
        else:
            min_r[i] = r

    # 右からmin_rを求める
    for i in range(N - 2, -1, -1):
        min_r[i] = min(min_r[i], min_r[i + 1] + 1)
    # print(min_r)

    answer = 0
    for i in range(N):
        answer += R[i] - min_r[i]
    print(answer)
