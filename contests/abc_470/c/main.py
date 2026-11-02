N, Q = map(int, input().split())

answer = 0
A = [0] * N
plus_index_set: set[int] = set()
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        x = q[1]
        x -= 1
        answer ^= A[x]
        A[x] += 1
        answer ^= A[x]
        if A[x] == 1:
            plus_index_set.add(x)
    elif q[0] == 2:
        new_plus_index_set: set[int] = set()
        for i in plus_index_set:
            answer ^= A[i]
            A[i] -= 1
            answer ^= A[i]
            if A[i] > 0:
                new_plus_index_set.add(i)
        plus_index_set = new_plus_index_set

    print(answer)
