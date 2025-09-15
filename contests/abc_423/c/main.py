N, R = map(int, input().split())
L = list(map(int, input().split()))

# most_left_0_index

num_0 = 0
num_1 = 0
for l in L:
    if l == 0:
        num_0 += 1
    else:
        num_1 += 1

if num_1 == N:
    print(0)
    exit()

most_left_0_index = 0
for i in range(N):
    if L[i] == 0:
        most_left_0_index = i
        break
most_right_0_index = N - 1
for i in range(N):
    index = N - 1 - i
    if L[index] == 0:
        most_right_0_index = index
        break

# print(most_left_0_index, most_right_0_index)
answer = 0
if R < most_left_0_index:
    answer += (most_left_0_index - R) * 2

if most_right_0_index + 1 < R:
    answer += (R - most_right_0_index - 1) * 2

num_1 -= most_left_0_index
num_1 -= N - most_right_0_index - 1

answer += num_0 + num_1 * 2
print(answer)
