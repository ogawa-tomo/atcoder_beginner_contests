C = int(input())
for _ in range(C):
    N, H = map(int, input().split())
    max_H = H
    min_H = H
    T = 0
    success = True
    for _ in range(N):
        t, l, u = map(int, input().split())
        dt = t - T

        # 飛んでいける高度の上限・下限
        max_H += dt
        min_H -= dt
        min_H = max(0, min_H)

        # 条件
        if max_H < l or min_H > u:
            success = False

        # 飛べる上限と下限
        max_H = min(max_H, u)
        min_H = max(min_H, l)

        T += dt

    if success:
        print("Yes")
    else:
        print("No")
