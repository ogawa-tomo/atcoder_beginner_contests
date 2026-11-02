N, Q = map(int, input().split())
P = [0]
P.extend(list(map(int, input().split())))

value_by_index: dict[int, int] = dict()
index_by_value: dict[int, int] = dict()
for i in range(1, N + 1):
    p = P[i]
    value_by_index[i] = p
    index_by_value[p] = i


# print(P)
inverse_count = 0
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        x = q[1]
        y = q[2]

        if inverse_count % 2 == 0:
            value_x = value_by_index[x]
            value_y = value_by_index[y]
            value_by_index[x] = value_y
            value_by_index[y] = value_x
            index_by_value[value_x] = y
            index_by_value[value_y] = x
        else:
            index_x = index_by_value[x]
            index_y = index_by_value[y]
            index_by_value[x] = index_y
            index_by_value[y] = index_x
            value_by_index[index_x] = y
            value_by_index[index_y] = x

    elif q[0] == 2:
        inverse_count += 1

answer: list[int] = []
for i in range(1, N + 1):
    if inverse_count % 2 == 0:
        answer.append(value_by_index[i])
    else:
        answer.append(index_by_value[i])
print(*answer)
