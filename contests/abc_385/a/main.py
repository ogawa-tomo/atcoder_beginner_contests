A, B, C = map(int, input().split())

if A + B == C:
    print("Yes")
    exit()
if A + C == B:
    print("Yes")
    exit()
if B + C == A:
    print("Yes")
    exit()

if A == B and B == C:
    print("Yes")
    exit()
print("No")