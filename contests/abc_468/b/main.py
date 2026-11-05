M, D = map(int, input().split())
S = list(input())

g_indice: list[int] = []
for i in range(M):
    s = S[i]
    if s == "G":
        g_indice.append(i)

for index in g_indice:
    for i in range(index - D, index + D + 1):
        if i < 0 or M <= i:
            continue
        S[i] = "G"

# print(S)
answer = 0
for s in S:
    if s == ".":
        answer += 1
print(answer)
