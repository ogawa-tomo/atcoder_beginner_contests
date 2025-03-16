N = int(input())
A = list(map(int, input().split()))

all_kinds = 0
first_half_dict: dict[int, int] = {}
second_half_dict: dict[int, int] = {}
for a in A:
    if a in first_half_dict:
        second_half_dict[a] += 1
    else:
        first_half_dict[a] = 0
        second_half_dict[a] = 1
        all_kinds += 1

# print(num_dict)
# print(all_kinds)

# i文字目以前と後に区切ったとき
first_half_kinds = 0
second_half_kinds = all_kinds
answer = 0
for i in range(N - 1):
    num = A[i]
    first_half_dict[num] += 1
    if first_half_dict[num] == 1:
        first_half_kinds += 1
    second_half_dict[num] -= 1
    if second_half_dict[num] == 0:
        second_half_kinds -= 1
    answer = max(answer, first_half_kinds + second_half_kinds)

print(answer)
