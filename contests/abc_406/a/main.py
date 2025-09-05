A, B, C, D = map(int, input().split())

if A < C:
    print("No")
    exit()

if C < A:
    print("Yes")
    exit()

if B < D:
    print("No")
else:
    print("Yes")
