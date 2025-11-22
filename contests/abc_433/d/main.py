from collections import defaultdict

N, M = map(int, input().split())
# A = list(map(int, input().split()))
A = list(input().split())
# print(A)

# d[i]: i桁の数字のリスト
d: defaultdict[int, list[str]] = defaultdict(list[str])
for a in A:
    d[len(a)].append(a)
# print(d)

answer = 0
for i1 in d:
    for i2 in d:
        # i1+i2桁の数を考えることになる
        if i1 + i2 < len(str(M)):
            continue
        i1_nums = d[i1]
# # print(16183 % 7)
# for i in range(100):
#     print(11 * i)

# # print(183183 / 7)
