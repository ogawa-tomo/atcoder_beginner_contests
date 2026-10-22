N, M = map(int, input().split())

answer = [0] * N

for i in range(M):
    answer[i % N] += 1

for a in answer:
    print(a)
