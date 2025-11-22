N = int(input())
A = list(map(int, input().split()))

answer: list[int] = []
for i in range(N):
    if i == 0:
        # answer.append(-1)
        print(-1)
        continue
    exists = False
    for j in range(i - 1, -1, -1):
        if A[j] > A[i]:
            # answer.append(j - 1)
            print(j + 1)
            exists = True
            break
    if not exists:
        # answer.append(-1)
        print(-1)

# print
