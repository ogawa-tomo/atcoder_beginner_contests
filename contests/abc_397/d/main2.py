N = int(input())


def func(d, y):
    return 3 * d * (y**2) + 3 * (d**2) * y + d**3 - N


for d in range(1, int(N ** (1 / 3)) + 1):
    # これがないとTLE
    if not ((d**3 - N) / (3 * d)).is_integer():
        continue

    # func(d, y)が0未満ならOK
    ok = 0
    ng = N
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if func(d, mid) <= 0:
            ok = mid
        else:
            ng = mid
    if func(d, ok) == 0 and ok > 0:
        print(d + ok, ok)
        exit()

print(-1)
