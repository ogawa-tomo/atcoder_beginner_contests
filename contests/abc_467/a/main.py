from fractions import Fraction

H, W = map(int, input().split())

obesity = Fraction(W, Fraction(H, 100) ** 2)
# print(obesity)
# print(float(obesity))
if obesity >= 25:
    print("Yes")
else:
    print("No")
