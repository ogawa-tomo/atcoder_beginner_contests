N = int(input())
A = list(map(int, input().split()))

A.sort()

answer: list[int] = []
for i in range(N):
    a = A[i]
    if i == 0:
        answer.append(a)
        continue
    prev = A[i - 1]
    if a == prev:
        continue
    answer.append(a)

print(len(answer))
print(" ".join([str(a) for a in answer]))
