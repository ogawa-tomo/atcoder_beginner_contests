N, M = map(int, input().split())
A = list(map(int, input().split()))

size = 0
for a in A:
    size += a

if size <= M:
    print("Yes")
else:
    print("No")
