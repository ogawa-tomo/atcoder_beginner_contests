K = int(input())
A = list(map(int, input().split()))

if 9 not in A:
    print(-1)
else:
    print(min(A))
