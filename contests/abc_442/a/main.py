S = list(input())

answer = 0
for s in S:
    if s == "i" or s == "j":
        answer += 1

print(answer)
