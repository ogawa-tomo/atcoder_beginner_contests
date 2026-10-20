N = int(input())
S = list(input())

answer = 0
i = 0
while i < N:
    s = S[i]
    if s != "R":
        i += 1
        continue
    num = 1
    while i < N - 1 and S[i + 1] == "R":
        num += 1
        i += 1
    answer = max(answer, num)
    i += 1

print(answer)
