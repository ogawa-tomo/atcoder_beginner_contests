X, Y = map(int, input().split())

month = (X + Y) % 12

if month == 0:
    print(12)
else:
    print(month)
