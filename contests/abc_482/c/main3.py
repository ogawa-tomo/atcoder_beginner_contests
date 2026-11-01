from typing import Callable


# 二分探索
def most_right_ok(min_i: int, max_i: int, ok_func: Callable[[int], bool]):
    ok = min_i - 1
    ng = max_i + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if ok_func(mid):
            ok = mid
        else:
            ng = mid
    if ok < min_i:
        return None
    return ok


# 二分探索
def most_left_ok(min_i: int, max_i: int, ok_func: Callable[[int], bool]):
    ok = max_i + 1
    ng = min_i - 1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if ok_func(mid):
            ok = mid
        else:
            ng = mid
    if ok > max_i:
        return None
    return ok


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

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        u = q[1]
        d = q[2]
        u -= 1
        d -= 1

        min_i = most_left_ok(0, N - 1, lambda i: u <= rows[i])
        max_i = most_right_ok(0, N - 1, lambda i: rows[i] <= d)
        # max_i < min_i になることはあり得るが、差は1になるので、結果的にmax_i - min_i + 1は0になって一致する
        # if min_i is None or max_i is None or max_i < min_i:
        if min_i is None or max_i is None:
            print(0)
        else:
            print(max_i - min_i + 1)

    elif q[0] == 2:
        l = q[1]
        r = q[2]
        l -= 1
        r -= 1

        min_i = most_left_ok(0, N - 1, lambda i: l <= columns[i])
        max_i = most_right_ok(0, N - 1, lambda i: columns[i] <= r)
        if min_i is None or max_i is None:
            print(0)
        else:
            print(max_i - min_i + 1)
