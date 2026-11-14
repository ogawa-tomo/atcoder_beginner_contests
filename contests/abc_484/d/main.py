# WA
from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))

answer = (N * (N - 1) // 2) + 1

# count_by_num[n]: nが登場した回数
count_by_num: defaultdict[int, int] = defaultdict(int)
for a in A:
    answer -= count_by_num[a]
    count_by_num[a] += 1

print(answer)
