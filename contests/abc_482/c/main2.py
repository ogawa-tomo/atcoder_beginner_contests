H, W, N, Q = map(int, input().split())

rows: list[int] = []
columns: list[int] = []
for _ in range(N):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    rows.append(r)
    columns.append(c)

rows.sort()
columns.sort()


def get_min_i(rc: int, rows_or_columns: list[int]):
    ok = N
    ng = -1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if rc <= rows_or_columns[mid]:
            ok = mid
        else:
            ng = mid
    return ok


def get_max_i(rc: int, rows_or_columns: list[int]):
    ok = -1
    ng = N
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if rows_or_columns[mid] <= rc:
            ok = mid
        else:
            ng = mid
    return ok


for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        u = q[1]
        d = q[2]
        u -= 1
        d -= 1

        min_i = get_min_i(u, rows)
        max_i = get_max_i(d, rows)
        # max_i < min_i になることはあり得るが、差は1になるので、結果的にmax_i - min_i + 1は0になって一致する
        # if max_i < 0 or N <= min_i or max_i < min_i:
        if max_i < 0 or N <= min_i:
            print(0)
        else:
            print(max_i - min_i + 1)

    elif q[0] == 2:
        l = q[1]
        r = q[2]
        l -= 1
        r -= 1
        min_i = get_min_i(l, columns)
        max_i = get_max_i(r, columns)
        # if max_i < 0 or N <= min_i or max_i < min_i:
        if max_i < 0 or N <= min_i:
            print(0)
        else:
            print(max_i - min_i + 1)
