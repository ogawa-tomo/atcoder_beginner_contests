N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
max_num = max(A)
# total = sum(A)
accum_sum: list[int] = []
for i, a in enumerate(A):
    if i == 0:
        accum_sum.append(a)
        continue
    accum_sum.append(accum_sum[i - 1] + a)
# print(accum_sum)


# Aの値がnum未満になる最大のインデックスを二分探索で求める
def max_index_larger_than(num):
    ok = -1
    ng = N
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if A[mid] < num:
            ok = mid
        else:
            ng = mid
    return ok


for _ in range(Q):
    b = int(input())
    if b > max_num:
        print(-1)
        continue
    index = max_index_larger_than(b - 1)
    # print(index)
    answer = 0
    if index >= 0:
        answer += accum_sum[index]
    answer += (b - 1) * (N - 1 - index)
    answer += 1
    print(answer)
