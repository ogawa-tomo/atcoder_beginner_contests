from collections import defaultdict
import math

N = int(input())
A = list(map(int, input().split()))

# sum_A = sum(A)

# d[i]: iが出現した回数
d: defaultdict[int, int] = defaultdict(int)
for a in A:
    d[a] += 1

# print(d)
answer = 0
for i in d:
    num_i = d[i]
    answer += math.comb(num_i, 2) * (N - num_i)

print(answer)
