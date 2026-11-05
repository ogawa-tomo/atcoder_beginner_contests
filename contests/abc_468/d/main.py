S = input()
N = len(S)

answer = 0

# dp[i][j]: j文字目からi文字後まで続く文字列の性質
dp: list[list[str]] = []
for i in range(N):
    if i == 0:
        dp.append(["p"] * N)  # 1文字は回文
        answer += N
    elif i == 1:
        row: list[str] = []
        for j in range(N - 1):
            if S[j] == S[j + 1]:
                row.append("p")  # 回文
            else:
                row.append("g")  # 回文ではない良い文
        dp.append(row)
        answer += N - 1
    else:
        dp.append([""] * (N - i))

# for row in dp:
#     print(row)

for i in range(2, N):
    for j in range(N - i):
        # j文字目からi文字後まで続く文字列
        match dp[i - 2][j + 1]:
            case "x":
                dp[i][j] = "x"
            case "g":
                if S[j] == S[j + i]:
                    dp[i][j] = "g"
                    answer += 1
                else:
                    dp[i][j] = "x"
            case "p":
                answer += 1
                if S[j] == S[j + i]:
                    dp[i][j] = "p"
                else:
                    dp[i][j] = "g"


# for row in dp:
#     print(row)

print(answer)
