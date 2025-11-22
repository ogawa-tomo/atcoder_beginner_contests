X, Y, Z = map(int, input().split())


while True:
    rate = X / Y
    if rate.is_integer() and rate == Z:
        print("Yes")
        exit()
    if rate < Z:
        print("No")
        exit()
    X += 1
    Y += 1
