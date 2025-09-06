import sys

N, M = map(int, input().split())

# 累積和
wall_sum: list[int] = [0] * N

for _ in range(M):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    wall_sum[l] += 1
    if r < N - 1:
        wall_sum[r + 1] -= 1

# print(wall_sum)
min_wall_num = sys.maxsize
wall_num = 0
for s in wall_sum:
    wall_num += s
    min_wall_num = min(wall_num, min_wall_num)

print(min_wall_num)
