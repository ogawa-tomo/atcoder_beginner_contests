S, A, B, X = map(int, input().split())

itr = X // (A + B)
amari = X % (A + B)

print(S * A * itr + S * min(amari, A))
