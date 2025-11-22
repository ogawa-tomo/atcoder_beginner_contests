S = list(map(int, list(input())))
# print(S)

answer = 0
for i in range(len(S) - 1):
    # if S[i] == 1 and S[i + 1] == 2:
    if S[i] + 1 == S[i + 1]:
        answer += 1
        j = 1
        while True:
            if (
                i - j >= 0
                and S[i - j] == S[i]
                and i + 1 + j < len(S)
                and S[i + 1 + j] == S[i + 1]
            ):
                answer += 1
                j += 1
            else:
                break

print(answer)
