import math
from collections import defaultdict

N = int(input())

# answer_dict[i]: 2乗和がiになる組み合わせの数
answer_dict: defaultdict[int, int] = defaultdict(int)

for i in range(1, math.isqrt(N) + 1):
    for j in range(i + 1, math.isqrt(N - i**2) + 1):
        power_sum = i**2 + j**2
        answer_dict[power_sum] += 1

answers: list[int] = []
for key in answer_dict:
    if answer_dict[key] == 1:
        answers.append(key)
answers.sort()
print(len(answers))
print(*answers)
