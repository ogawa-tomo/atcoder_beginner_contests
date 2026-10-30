from collections import defaultdict


N, K = map(int, input().split())
A = list(map(int, input().split()))

num_by_class: defaultdict[int, int] = defaultdict(int)
for k in range(K):
    num_by_class[k] = 0
for i in range(N):
    a = A[i]
    a -= 1
    num_by_class[a] += 1

num_list = list(num_by_class.values())
# print(num_list)

max_num = max(num_list)
answer = 0
for num in num_list:
    if num >= max_num - 1:
        answer += 1

print(answer)
