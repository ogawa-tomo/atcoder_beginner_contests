from collections import defaultdict

N, K = map(int, input().split())
S = input()

d: defaultdict[str, int] = defaultdict(int)
for i in range(N - K + 1):
    s = S[i : i + K]
    # print(s)
    d[s] += 1

# print(d)
max_value = max(d.values())
print(max_value)
strings: list[str] = []
for key in d:
    if d[key] == max_value:
        strings.append(key)

strings.sort()
print(" ".join(strings))
