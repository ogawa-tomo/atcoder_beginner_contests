N, K, X = map(int, input().split())

strings_list: list[str] = []
for _ in range(N):
    strings = input()
    strings_list.append(strings)

strings_candidates: list[str] = []

# 全探索
for i in range(N**K):
    current_strings: str = ""
    # iをK桁のN進法の数字とみなして、k桁目の数を調べる
    for k in range(K):
        num = (i // N**k) % N  # Nのk乗で割った商の、さらにNのあまりをとったもの
        current_strings += strings_list[num]
    strings_candidates.append(current_strings)

strings_candidates.sort()
print(strings_candidates[X - 1])
