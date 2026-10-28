N = int(input())
P = list(map(int, input().split()))

for i in range(N):
    group_num = i // 10
    min_num = 10 * group_num
    max_num = min_num + 9

    p = P[i]
    p -= 1
    if p < min_num or max_num < p:
        print("No")
        exit()

print("Yes")
