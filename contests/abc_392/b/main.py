N, M = map(int, input().split())
A = list(map(int, input().split()))

answer = []
for i in range(1, N + 1):
    if i not in A:
        answer.append(str(i))

print(len(answer))
print(" ".join(answer))
