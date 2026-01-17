N, K, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
# print(A)
s = sum(A[:K])
# print(s)
if X > s:
    print(-1)
    exit()

sake_list = A[:K]
sake_list.sort(reverse=True)
# print(sake_list)

answer = N - K
# print(other_num)
sake_amount = 0
for a in sake_list:
    sake_amount += a
    answer += 1
    if sake_amount >= X:
        print(answer)
        exit()
