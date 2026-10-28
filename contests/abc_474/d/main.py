N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer: list[int] = []
minus_total = 0
plus_total = 0
for i in range(N):
    diff = A[i] - B[i]
    if diff > 0:
        plus_total += diff
        answer.append(10**18)
    elif diff < 0:
        minus_total -= diff
        answer.append(1)
    else:
        answer.append(1)

if plus_total * 10**18 > minus_total:
    print("Yes")
    print(*answer)
else:
    print("No")
