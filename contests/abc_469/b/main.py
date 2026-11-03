N = int(input())
S = input()

answer = 0
for i in range(N):
    s = S[i]

    if s != "x":
        continue

    if i == 0:
        left_ok = True
    else:
        left_ok = S[i - 1] == "x"

    if i == N - 1:
        right_ok = True
    else:
        right_ok = S[i + 1] == "x"

    if left_ok and right_ok:
        answer += 1

print(answer)
