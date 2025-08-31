S = list(input())

answer: list[str] = []

for s in S:
    if s.isupper():
        answer.append(s)

print("".join(answer))
