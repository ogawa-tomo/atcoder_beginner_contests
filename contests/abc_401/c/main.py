N, K = map(int, input().split())
mod = 10**9

plus_arr = [1] * K
plus_value = K
a = 0
for i in range(N + 1):
    if i < K:
        a = 1
    else:
        a = plus_value
        index = i % K
        plus_value -= plus_arr[index]
        plus_value += a
        plus_arr[index] = a
        a %= mod
        plus_value %= mod

print(a)
