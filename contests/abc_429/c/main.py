N = int(input())
A = list(map(int, input().split()))

# sum_A = sum(A)

# d[i]: iが出現した回数
d: dict[int, int] = {}
for a in A:
    if a not in d:
        d[a] = 1
    else:
        d[a] += 1

# print(d)
answer = 0
for i in d:
    answer += (d[i] * (d[i] - 1) // 2) * (N - d[i])

print(answer)
