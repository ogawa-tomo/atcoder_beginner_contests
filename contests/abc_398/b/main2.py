A = list(map(int, input().split()))

# num_list[i]: iの枚数
num_list = [0] * 14

for a in A:
    num_list[a] += 1


over_2_nums: list[int] = []
exists_3_num = False
for num in num_list:
    if num >= 2:
        over_2_nums.append(num)
    if num >= 3:
        exists_3_num = True

if exists_3_num and len(over_2_nums) >= 2:
    print("Yes")
else:
    print("No")
