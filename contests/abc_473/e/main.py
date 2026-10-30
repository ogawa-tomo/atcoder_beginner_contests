# WA
N, K = map(int, input().split())
A = list(map(int, input().split()))

left = 0
right = 0
value = A[0]
answer = 0
while left < N and right < N:
    # print(left, right)
    # print(value)
    if value % K == 0:
        answer += 1
        right += 1
        if right >= N:
            break
        left = right
        value = A[left]
        continue

    while right < N and value < K:
        right += 1
        if right >= N:
            break
        value += A[right]
        # print(left, right)

    if value > K:
        value -= A[left]
        left += 1

print(answer)
