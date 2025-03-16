# これはTLE
import math

N = int(input())

x_min = int(math.pow(N, 1 / 3))
N_max = 10**18

eps = 0.000000001

for x in range(x_min, N_max + 1):
    if x * (x - 1) > (N - 1) / 3:
        break
    y_3 = math.pow(x, 3) - N
    # print(y_3)
    if y_3 <= 0:
        continue

    y = math.pow(y_3, 1 / 3)
    if y - int(y) < eps:
        print(x, int(y))
        exit()
    # y = int(math.pow(y_3, 1 / 3))
    # if x**3 - y**3 == N:
    #     print(x, y)
    #     exit()
    # if x**3 - (y + 1) ** 3 == N:
    #     print(x, y + 1)
    #     exit()

print(-1)
