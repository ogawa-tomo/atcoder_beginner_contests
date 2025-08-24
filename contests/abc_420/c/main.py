# 難しく考えすぎた…
N, Q = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = 0
min_list: list[int] = []
# max_list: list[int] = []
for i in range(N):
    min_value = min(A[i], B[i])
    # max_list.append(max(A[i], B[i]))
    min_list.append(min_value)
    answer += min_value


for _ in range(Q):
    query = input().split()
    # print(query)
    c = query[0]
    x = int(query[1])
    v = int(query[2])
    x -= 1
    # v -= 1

    if c == "A":
        if A[x] < B[x]:
            if v < A[x]:
                answer -= A[x] - v
                min_list[x] = v
            elif v < B[x]:
                answer += v - A[x]
                min_list[x] = v
            else:
                # B[x] <= v
                answer += B[x] - A[x]
                min_list[x] = B[x]
        elif A[x] == B[x]:
            if v < A[x]:
                answer -= A[x] - v
                min_list[x] = v
        else:  # B[x] <= A[x]:
            if v < B[x]:
                answer -= B[x] - v
                min_list[x] = v
            elif v < A[x]:
                pass
            else:
                pass
        A[x] = v
    else:
        if B[x] <= A[x]:
            if v < B[x]:
                answer -= B[x] - v
                min_list[x] = v
            elif v < A[x]:
                answer += v - B[x]
                min_list[x] = v
            else:
                answer += A[x] - B[x]
                min_list[x] = A[x]
        elif A[x] == B[x]:
            if v < B[x]:
                answer -= B[x] - v
                min_list[x] = v
        else:
            if v < A[x]:
                answer -= A[x] - v
                min_list[x] = v
        B[x] = v
    # print(A)
    # print(B)
    print(answer)
