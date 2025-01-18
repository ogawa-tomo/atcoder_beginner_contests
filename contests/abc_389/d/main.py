import math

R = int(input())

h = R / math.sqrt(2)

answer = (int(h - 0.5) * 2 + 1) ** 2

for i in range(int(h - 0.5) + 1, R):
    x = i + 0.5
    y = math.sqrt(R**2 - x**2)
    answer += int(y - 0.5) * 8 + 4
print(answer)
