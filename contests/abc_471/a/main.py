A, B = map(int, input().split())

plus = A + B
minus = A - B
mult = A * B
q = A // B
r = A % B

if plus == 9 or minus == 9 or mult == 9 or (q == 9 and r == 0):
    print("Nine")
else:
    print("Nein")
