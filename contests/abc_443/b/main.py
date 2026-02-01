N, K = map(int, input().split())

year = 0
beans = 0
age = N
while True:
    beans += age
    if beans >= K:
        print(year)
        exit()
    age += 1
    year += 1
