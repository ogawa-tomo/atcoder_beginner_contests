import math

N = int(input())

for d in range(1, int(N ** (1 / 3)) + 1):
    y = (-3 * (d**2) + math.sqrt(9 * (d**4) - 4 * 3 * d * (d**3 - N))) / (6 * d)
    if y.is_integer() and y > 0:
        print(int(y) + d, int(y))
        exit()

print(-1)
