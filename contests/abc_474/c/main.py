N, Q = map(int, input().split())
P = list(map(int, input().split()))

index_by_num: dict[int, int] = dict()
for i in range(N):
    index = i + 1
    p = P[i]
    index_by_num[p] = index

max_index = N + 1
for _ in range(Q):
    a = int(input())
    index_by_num[a] = max_index
    max_index += 1


num_by_index: dict[int, int] = dict()
for num in index_by_num:
    index = index_by_num[num]
    num_by_index[index] = num

indice = list(num_by_index.keys())
indice.sort()
answers = [num_by_index[index] for index in indice]
print(*answers)
