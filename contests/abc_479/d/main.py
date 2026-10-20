import sys

N, Q = map(int, input().split())
L_ = list(map(int, input().split()))
R = list(map(int, input().split()))

L = [0]
L.extend(L_)


# min_R[i]: i以下で最も小さいR
min_R: list[int] = []
for i in range(N - 1):
    if i == 0:
        min_R.append(R[i])
    else:
        min_R.append(min(min_R[i - 1], R[i]))

# min_L[i]: i以上で最も小さいL
min_L = [0] * N
for i in range(N - 1, 0, -1):
    if i == N - 1:
        min_L[i] = L[N - 1]
    else:
        min_L[i] = min(L[i], min_L[i + 1])

# print(min_R)
# print(min_L)

for _ in range(Q):
    s, t = map(int, input().split())
    s -= 1
    t -= 1

    if s < t:
        # 右に行く

        # 直接
        answer1 = R[s]

        answer2 = sys.maxsize
        if 0 < s:
            # 左に行って、右に行く
            answer2 = L[s] + min_R[s - 1]

        answer = min(answer1, answer2)

    else:
        # 左に行く

        # 直接
        answer1 = L[s]

        answer2 = sys.maxsize
        # 右に行って、左に行く
        if s < N - 1:
            answer2 = R[s] + min_L[s + 1]

        answer = min(answer1, answer2)

    print(answer)
