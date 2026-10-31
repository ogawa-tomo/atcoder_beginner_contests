N = int(input())
X = list(map(int, input().split()))

min_x = X[0]
max_x = X[N - 1]
for k in range(N):
    if k == 0 or k == N - 1:
        print((max_x - min_x) // 2)
        continue

    x = X[k]

    # 右に行くケース
    right_x = X[k + 1]
    mid_x = (x + right_x) // 2  # 中間地点
    time_r = (right_x - x) // 2  # 中間地点までかかる時間

    most_left = min_x + time_r  # 左端のひと
    most_right = max_x - time_r  # 左端のひと

    time_r += max((most_right - mid_x) // 2, (mid_x - most_left) // 2)

    # 左に行くケース
    left_x = X[k - 1]
    mid_x = (x + left_x) // 2
    time_l = (x - left_x) // 2

    most_left = min_x + time_l
    most_right = max_x - time_l

    time_l += max((most_right - mid_x) // 2, (mid_x - most_left) // 2)

    print(min(time_r, time_l))
