T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort()
    overflow_num = 0
    b_i = 0
    for i in range(N):
        a = A[i]
        while b_i < N and a + B[b_i] < M:
            b_i += 1
        if b_i >= N:
            break
        overflow_num += 1
        b_i += 1
    print(sum(A) + sum(B) - overflow_num * M)
