import math
from collections import defaultdict

N = int(input())

answers: set[int] = set()
for i in range(1, math.isqrt(N) + 1):
    for j in range(i + 1, math.isqrt(N - i**2) + 1):
        answer = i**2 + j**2
        if answer in answers:
            answers.remove(answer)
        else:
            answers.add(answer)

answer_list = list(answers)
answer_list.sort()
print(len(answer_list))
print(*answer_list)
