N, M = map(int, input().split())

# score[i]: 人iのスコア
score = [0] * N

# votes[i][j]: 人iのj回目の投票
votes: list[list[str]] = []
for _ in range(N):
    votes.append(list(input()))

    # print(S)
# print(votes)

for j in range(M):
    # j回目の投票
    num_0 = 0
    num_1 = 0
    for i in range(N):
        if votes[i][j] == "0":
            num_0 += 1
        else:
            num_1 += 1
    if num_0 == 0 or num_1 == 0:
        for i in range(N):
            score[i] += 1
        continue
    if num_0 < num_1:
        for i in range(N):
            if votes[i][j] == "0":
                score[i] += 1
        continue
    if num_1 < num_0:
        for i in range(N):
            if votes[i][j] == "1":
                score[i] += 1

max_score = max(score)

max_scorers: list[str] = []
for i in range(N):
    if score[i] == max_score:
        max_scorers.append(str(i + 1))

print(" ".join(max_scorers))
