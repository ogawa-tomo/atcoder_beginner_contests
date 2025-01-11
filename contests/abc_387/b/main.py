X = int(input())

answer = 0
for a in range(1, 10):
    for b in range(1, 10):
        seki = a * b
        if seki != X:
            answer += seki
print(answer)
