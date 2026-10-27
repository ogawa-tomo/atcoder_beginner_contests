S = input()

answer: list[str] = []
for s in S:
    answer.append(s)
    answer.append("o")

answer.pop()
print("".join(answer))
