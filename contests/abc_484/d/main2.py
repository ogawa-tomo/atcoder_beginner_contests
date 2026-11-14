# AC
from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))

answer = (N * (N - 1) // 2) + 1

# count_by_num[n]: nが登場した回数
count_by_num: defaultdict[int, int] = defaultdict(int)
for i in range(N):
    a = A[i]
    if i > 0 and A[i - 1] == a:
        answer -= i
    else:
        answer -= count_by_num[a]
    count_by_num[a] += 1

print(answer)
