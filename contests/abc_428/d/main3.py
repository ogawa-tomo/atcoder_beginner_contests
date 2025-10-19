# AC
# でもCPythonだとTLE
import math

T = int(input())
for _ in range(T):
    C, D = map(int, input().split())
    answer = 0
    # C+xがd桁のときに条件に合う数を調べる
    d_max = math.floor(math.log10(C + D)) + 1
    for d in range(1, d_max + 1):
        # C+xがd桁であるための条件
        x_min = 10 ** (d - 1) - C
        x_max = 10**d - 1 - C
        # かつ、問題の制約より1<=x<=D
        x_min = max(x_min, 1)
        x_max = min(x_max, D)
        if x_min > x_max:
            continue
        # C+xがd桁であるという前提のもとでのf
        f_min = C * 10**d + C + x_min
        f_max = C * 10**d + C + x_max
        # f_min以上f_max以下の平方数の数を調べればよい
        # math.sqrtを使うと誤差が出てWA!
        # answer += math.floor(math.sqrt(f_max)) - math.floor(math.sqrt(f_min - 1))
        # math.isqrtを使う
        answer += math.isqrt(f_max) - math.isqrt(f_min - 1)
    print(answer)
