# どうしてWAなのか分からねぇ…
T = int(input())
for _ in range(T):
    na, nb, nc = map(int, input().split())
    abc_num = min(na, nb, nc)
    # print(abc_num)
    na -= abc_num
    nb -= abc_num
    nc -= abc_num
    # print(na, nb, nc)
    if na == 0 or nc == 0:
        print(abc_num)
        continue
    max_ac = max(na, nc)
    min_ac = min(na, nc)
    if max_ac // 2 >= min_ac:
        print(abc_num + min_ac)
        continue
    aac_or_acc_num = max_ac // 2
    max_ac -= aac_or_acc_num * 2
    min_ac -= aac_or_acc_num
    if max_ac == 1 and min_ac >= 2:
        aac_or_acc_num += 1
    print(abc_num + aac_or_acc_num)
# print("hoge")
# print(7 // 2)
