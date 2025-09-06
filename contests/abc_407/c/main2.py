# AC
S = list(map(int, input()))

answer = 0
for i in range(len(S)):
    index = len(S) - i - 1
    S[index] = (S[index] - answer) % 10
    answer += S[index]

print(answer + len(S))
