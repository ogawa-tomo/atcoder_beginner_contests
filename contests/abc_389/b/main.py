import math

X = int(input())
N = 2
while True:
    if math.factorial(N) == X:
        print(N)
        exit()
    N += 1
