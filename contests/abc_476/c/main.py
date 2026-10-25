N = int(input())
A = list(map(int, input().split()))

current = A[:2]
current.sort(reverse=True)
for k in range(2, N):
    a = A[k]
    current.append(a)
    current.sort(reverse=True)
    current = current[:3]
    print(current[-1])
