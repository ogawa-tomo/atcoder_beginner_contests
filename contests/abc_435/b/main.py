N = int(input())
A = list(map(int, input().split()))

answer = 0
for l in range(N):
    for r in range(l, N):
        a_sum = 0
        success = True
        for i in range(l, r + 1):
            a_sum += A[i]
        for i in range(l, r + 1):
            ai = A[i]
            if a_sum % ai == 0:
                success = False
                break
        if success:
            answer += 1

print(answer)
