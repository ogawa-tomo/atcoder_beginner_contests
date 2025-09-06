N, S = map(int, input().split())
T = list(map(int, input().split()))

for i in range(N):
    tap = T[i]
    if i == 0:
        last_tap = 0
    else:
        last_tap = T[i - 1]

    time = tap - last_tap
    if time > S + 0.5:
        print("No")
        exit()

print("Yes")
