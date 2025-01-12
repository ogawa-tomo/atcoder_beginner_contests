N = int(input())
A = list(map(int, input().split()))

answer = 0
for a in A:
    size = a * 2
    # 配列Aのなかで、大きさがsize以上である最小のインデックスを見つける
    ng = -1
    ok = N
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if A[mid] >= size:
            ok = mid
        else:
            ng = mid
    answer += N - ok

print(answer)
