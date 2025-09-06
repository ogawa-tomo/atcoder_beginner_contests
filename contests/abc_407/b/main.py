X, Y = map(int, input().split())

cases = 0
for i in range(1, 7):
    for j in range(1, 7):
        if i + j >= X:
            cases += 1
            continue
        if abs(i - j) >= Y:
            cases += 1

print(cases / 36)
