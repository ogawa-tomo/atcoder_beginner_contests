N, Q = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = 0
for i in range(N):
    min_value = min(A[i], B[i])
    answer += min_value


for _ in range(Q):
    query = input().split()
    c = query[0]
    x = int(query[1])
    v = int(query[2])
    x -= 1

    answer -= min(A[x], B[x])
    if c == "A":
        A[x] = v
    else:
        B[x] = v
    answer += min(A[x], B[x])
    print(answer)
