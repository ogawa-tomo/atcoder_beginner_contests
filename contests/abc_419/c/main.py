import math

N = int(input())
min_i = 10**9
max_i = 1
min_j = 10**9
max_j = 1

for _ in range(N):
    i, j = map(int, input().split())
    min_i = min(min_i, i)
    max_i = max(max_i, i)
    min_j = min(min_j, j)
    max_j = max(max_j, j)

time_i = math.ceil((max_i - min_i) / 2)
time_j = math.ceil((max_j - min_j) / 2)
print(max(time_i, time_j))
