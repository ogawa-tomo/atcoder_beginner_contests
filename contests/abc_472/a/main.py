S = input()

answer = ""
for s in S:
    if s != "A":
        answer += "."
    else:
        answer += s

print(answer)
