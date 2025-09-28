N = int(input())

answer = 0
for i in range(1, N + 1):
    answer += ((-1) ** i) * (i**3)
print(answer)
