N = int(input())
A = list(map(int, input().split()))

sumA = sum(A)

answer = sumA**2
for a in A:
    answer -= a**2

print(answer // 2)
