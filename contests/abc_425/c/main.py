N, Q = map(int, input().split())
A = list(map(int, input().split()))
current_index = 0
sum_A: list[int] = []
for i in range(N):
    if i == 0:
        sum_A.append(A[0])
    else:
        sum_A.append(sum_A[i - 1] + A[i])

# print(sum_A)
all_sum = sum(A)

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        c = q[1]
        current_index += c
        current_index %= N
        # print(current_index)
    else:
        l = q[1] - 1
        r = q[2] - 1
        l = (l + current_index) % N
        r = (r + current_index) % N
        if l <= r:
            if l == 0:
                print(sum_A[r])
            else:
                print(sum_A[r] - sum_A[l - 1])
        else:
            r_sum = sum_A[r]
            # if l == 0:
            #     l_sum = all_sum
            l_sum = all_sum - sum_A[l - 1]
            print(r_sum + l_sum)
