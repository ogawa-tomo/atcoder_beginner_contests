N = int(input())
A = list(map(int, input().split()))

total_coin_100 = 0
total_coin_10 = 0
total_coin_1 = 0

for a in A:
    a %= 1000

    change = 1000 - a % 1000
    if change == 1000:
        continue

    coin_100 = change // 100
    change -= coin_100 * 100
    total_coin_100 += coin_100

    coin_10 = change // 10
    change -= coin_10 * 10
    total_coin_10 += coin_10

    total_coin_1 += change

print(total_coin_1, total_coin_10, total_coin_100)
