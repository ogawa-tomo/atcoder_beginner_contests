# WA/TLE
import math

N = int(input())


answers: list[int] = []
for i in range(1, N + 1):
    if i**2 * 2 > N:
        break
    for j in range(i + 1, N + 1):
        tmp = i**2 + j**2
        if tmp > N:
            break
        answers.append(tmp)

# print(answers)
answers.sort()
print(len(answers))
print(*answers)
